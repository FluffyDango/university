#!/bin/bash

SSH_USER="rena9048"
NODES=("node0" "node1" "node2" "node3")
MINIO_HOST="node0:80"
MINIO_ACCESS_KEY="minioadmin"
MINIO_SECRET_KEY="minioadmin"
OUTPUT_DIR="./warp-results-$(date +%Y%m%d-%H%M%S)"
DURATION="5m"
FIXED_SIZE="128KiB"
FIXED_CONCURRENCY=64
FIXED_OBJECT_COUNT=25000
IS_MINIO_BEING_TESTED=false

mkdir -p "$OUTPUT_DIR"
echo "Results will be saved to: $OUTPUT_DIR"
echo "Started at: $(date)"

quick_cleanup() {
  echo "[Cleanup] Removing test objects..."
  # Use force to not get prompt of "are sure you want to remove it"
  # Works for both Minio and Ceph
  mc rm --recursive --force --quiet "myminio/warp-benchmark-bucket" 1>/dev/null
  echo "[Cleanup] Removed"
  sleep 2
}

drop_caches() {
  echo "[System] Dropping caches on all nodes..."
  for NODE in "${NODES[@]}"; do
    ssh $SSH_USER@$NODE "sync; echo 3 | sudo tee /proc/sys/vm/drop_caches >/dev/null"
  done
}

start_monitoring() {
  local test_label=$1
  echo "[Monitor] Starting system monitoring for: $test_label"

  # Adding 2>&1 because connection does not close if it is waiting for output.
  for NODE in "${NODES[@]}"; do
    ssh $SSH_USER@$NODE "
      nohup mpstat -P ALL 1 > /tmp/mpstat_${test_label}.log 2>&1 &
      nohup iostat -xz 1 > /tmp/iostat_${test_label}.log 2>&1 &
      nohup vmstat 1 > /tmp/vmstat_${test_label}.log 2>&1 &
      nohup sar -n DEV 1 > /tmp/net_${test_label}.log 2>&1 &
    "
  done
}

stop_monitoring() {
  local test_label=$1
  echo "[Monitor] Stopping and collecting data for: $test_label"
  mkdir -p "$OUTPUT_DIR/sysstat/$test_label"

  for NODE in "${NODES[@]}"; do
    ssh $SSH_USER@$NODE "pkill mpstat; pkill iostat; pkill vmstat; pkill sar" 2>/dev/null

    scp -q $SSH_USER@$NODE:/tmp/mpstat_${test_label}.log "$OUTPUT_DIR/sysstat/$test_label/mpstat_${NODE}.log"
    scp -q $SSH_USER@$NODE:/tmp/iostat_${test_label}.log "$OUTPUT_DIR/sysstat/$test_label/iostat_${NODE}.log"
    scp -q $SSH_USER@$NODE:/tmp/vmstat_${test_label}.log "$OUTPUT_DIR/sysstat/$test_label/vmstat_${NODE}.log"
    scp -q $SSH_USER@$NODE:/tmp/net_${test_label}.log "$OUTPUT_DIR/sysstat/$test_label/net_${NODE}.log"

    ssh $SSH_USER@$NODE "rm -rf /tmp/*" 2>/dev/null
  done
}

capture_storage_before() {
  local test_label=$1
  echo "[Storage] Capturing BEFORE metrics for: $test_label"

  mkdir -p "$OUTPUT_DIR/sysstat/$test_label"

  if $IS_MINIO_BEING_TESTED; then
    mc du myminio/warp-benchmark-bucket --json >"$OUTPUT_DIR/sysstat/$test_label/minio_logical_size_before.json"
    mc admin info myminio --json >"$OUTPUT_DIR/sysstat/$test_label/minio_physical_usage_before.json"
  else
    ssh $SSH_USER@${NODES[0]} "sudo ceph df detail --format json" >"$OUTPUT_DIR/sysstat/$test_label/ceph_df_before.json"
    ssh $SSH_USER@${NODES[0]} "sudo ceph osd df --format json" >"$OUTPUT_DIR/sysstat/$test_label/ceph_osd_df_before.json"
  fi

  for NODE in "${NODES[@]}"; do
    ssh $SSH_USER@$NODE "df -B1 /mnt/data" >"$OUTPUT_DIR/sysstat/$test_label/df_${NODE}_before.txt"
    ssh $SSH_USER@$NODE "df -i /mnt/data" >"$OUTPUT_DIR/sysstat/$test_label/df_inodes_${NODE}_before.txt"
    ssh $SSH_USER@$NODE "stat -f /mnt/data" >"$OUTPUT_DIR/sysstat/$test_label/stat_${NODE}_before.txt" 2>/dev/null || true
  done
}

capture_storage_after() {
  local test_label=$1
  echo "[Storage] Capturing AFTER metrics for: $test_label"

  if $IS_MINIO_BEING_TESTED; then
    mc du myminio/warp-benchmark-bucket --json >"$OUTPUT_DIR/sysstat/$test_label/minio_logical_size_after.json"
    mc admin info myminio --json >"$OUTPUT_DIR/sysstat/$test_label/minio_physical_usage_after.json"
  else
    ssh $SSH_USER@${NODES[0]} "sudo ceph df detail --format json" >"$OUTPUT_DIR/sysstat/$test_label/ceph_df_after.json"
    ssh $SSH_USER@${NODES[0]} "sudo ceph osd df --format json" >"$OUTPUT_DIR/sysstat/$test_label/ceph_osd_df_after.json"
  fi

  for NODE in "${NODES[@]}"; do
    ssh $SSH_USER@$NODE "df -B1 /mnt/data" >"$OUTPUT_DIR/sysstat/$test_label/df_${NODE}_after.txt"
    ssh $SSH_USER@$NODE "df -i /mnt/data" >"$OUTPUT_DIR/sysstat/$test_label/df_inodes_${NODE}_after.txt"
    ssh $SSH_USER@$NODE "stat -f /mnt/data" >"$OUTPUT_DIR/sysstat/$test_label/stat_${NODE}_after.txt" 2>/dev/null || true
  done
}

run_test() {
  local test_name=$1
  shift
  echo ""
  echo "-----------------------------------"
  echo "Running: $test_name"
  echo "Command: warp $@"
  echo "Started at: $(date)"
  echo "-----------------------------------"

  drop_caches

  capture_storage_before "$test_name"
  start_monitoring "$test_name"

  # Run the actual command
  if warp "$@" \
    --host="$MINIO_HOST" \
    --access-key="$MINIO_ACCESS_KEY" \
    --secret-key="$MINIO_SECRET_KEY" \
    --full \
    --analyze.dur="10s" \
    --analyze.out="$OUTPUT_DIR/analysis-${test_name}.csv" \
    --noclear; then
    echo "$test_name completed successfully"
  else
    echo "$test_name failed with exit code $?"
  fi

  stop_monitoring "$test_name"
  capture_storage_after "$test_name"

  sleep 5
}

echo ""
echo "1. Testing Various Object Sizes"

OBJECT_SIZES=("1KiB" "4KiB" "64KiB" "256KiB" "1MiB")

for size in "${OBJECT_SIZES[@]}"; do
  quick_cleanup

  run_test "PUT-${size}" put \
    --obj.size="$size" \
    --duration="$DURATION" \
    --concurrent=$FIXED_CONCURRENCY \
    --benchdata="$OUTPUT_DIR/put-size-${size}"

  run_test "GET-${size}" get \
    --obj.size="$size" \
    --objects=$FIXED_OBJECT_COUNT \
    --duration="$DURATION" \
    --concurrent=$FIXED_CONCURRENCY \
    --benchdata="$OUTPUT_DIR/get-size-${size}" \
    --list-existing

  quick_cleanup
done

echo ""
echo "2. Testing Various Client Counts"

CLIENT_COUNTS=(1 4 8 64 128)
# Runs for $DURATION time

for clients in "${CLIENT_COUNTS[@]}"; do
  quick_cleanup

  run_test "PUT-clients-${clients}" put \
    --obj.size="$FIXED_SIZE" \
    --duration="$DURATION" \
    --concurrent="$clients" \
    --benchdata="$OUTPUT_DIR/put-clients-${clients}"

  run_test "GET-clients-${clients}" get \
    --obj.size="$FIXED_SIZE" \
    --objects=$FIXED_OBJECT_COUNT \
    --duration="$DURATION" \
    --concurrent="$clients" \
    --benchdata="$OUTPUT_DIR/get-clients-${clients}" \
    --list-existing

  quick_cleanup
done

echo ""
echo "3. Testing Various Object Counts"

OBJECT_COUNTS=(100 500 1000 2500 10000)
# Runs for untill all objects are done

for obj_count in "${OBJECT_COUNTS[@]}"; do
  quick_cleanup

  run_test "PUT-objects-${obj_count}" put \
    --obj.size="$FIXED_SIZE" \
    --concurrent=$FIXED_CONCURRENCY \
    --benchdata="$OUTPUT_DIR/put-objects-${obj_count}"

  run_test "GET-objects-${obj_count}" get \
    --obj.size="$FIXED_SIZE" \
    --objects="$obj_count" \
    --concurrent=$FIXED_CONCURRENCY \
    --benchdata="$OUTPUT_DIR/get-objects-${obj_count}" \
    --list-existing

  quick_cleanup
done

echo ""
echo "4. Mixed Workload Test"

SIZE_BETWEEN="10KiB,1MiB"
# Runs for $DURATION time

run_test "MIXED-workload" mixed \
  --obj.size="$SIZE_BETWEEN" \
  --obj.randsize \
  --objects=$FIXED_OBJECT_COUNT \
  --duration="$DURATION" \
  --concurrent=$FIXED_CONCURRENCY \
  --benchdata="$OUTPUT_DIR/mixed-workload"

quick_cleanup

echo ""
echo "DONE"
