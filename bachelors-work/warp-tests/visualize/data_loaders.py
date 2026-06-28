import json
import pandas as pd
import zstandard as zstd
import io
from pathlib import Path


class DataLoader:
    @staticmethod
    def load_warp_csv(results_dir, test_name):
        csv_zst_file = Path(results_dir) / f'{test_name}.csv.zst'

        with open(csv_zst_file, 'rb') as f:
            dctx = zstd.ZstdDecompressor()
            with dctx.stream_reader(f) as reader:
                text_stream = io.TextIOWrapper(reader, encoding='utf-8')
                df = pd.read_csv(text_stream)

        # Column definitions:
        # idx - Sequential operation index
        # thread - Worker thread number that executed the operation
        # op - Operation type (GET, PUT, DELETE, STAT)
        # client_id - Unique identifier for the client session
        # n_objects - Number of objects involved in the operation (typically 1)
        # bytes - Size of the object in bytes (0 for STAT/DELETE operations)
        # endpoint - Target storage endpoint URL
        # file - Object path/key in the storage system
        # error - Error message if operation failed (empty if successful)
        # start - Timestamp when operation started (ISO 8601 with timezone)
        # first_byte - Timestamp when first byte received (GET only, empty for PUT/DELETE/STAT)
        # end - Timestamp when operation completed (ISO 8601 with timezone)
        # duration_ns - Total operation duration in nanoseconds
        # cat - Category/classification code (typically 0 for successful operations)

        return df

    @staticmethod
    def load_warp_analysis(results_dir, test_name):
        analysis_file = Path(results_dir) / f'analysis-{test_name}.csv'

        NUMERIC_COLUMNS = [
            'duration_s', 'objects_per_op', 'bytes', 'full_ops',
            'partial_ops', 'ops_started', 'ops_ended', 'errors',
            'mb_per_sec', 'ops_ended_per_sec', 'objs_per_sec', 'reqs_ended_avg_ms'
        ]

        try:
            df = pd.read_csv(analysis_file, sep='\t', engine='python')

            # Remove header repetitions (warp repeats 'op' in the data)
            df = df[df['op'] != 'op']
            df = df.reset_index(drop=True)

            # Convert numeric columns to proper types
            for col in NUMERIC_COLUMNS:
                if col in df.columns:
                    df[col] = pd.to_numeric(df[col], errors='coerce')

            # Column definitions:
            # index - Sequential row number for the time interval
            # op - Operation type (GET, PUT, DELETE, STAT)
            # host - Target storage endpoint URL
            # duration_s - Measurement interval duration in seconds
            # objects_per_op - Number of objects per operation (usually 1)
            # bytes - Total bytes transferred during this interval
            # full_ops - Operations completed successfully within the interval
            # partial_ops - Operations started but not completed in this interval
            # ops_started - Total operations initiated during this interval
            # ops_ended - Total operations completed during this interval
            # errors - Number of failed operations
            # mb_per_sec - Throughput in megabytes per second (bandwidth)
            # ops_ended_per_sec - Operations completed per second (IOPS)
            # objs_per_sec - Objects processed per second
            # reqs_ended_avg_ms - Average request latency in milliseconds
            # start_time - Interval start timestamp with timezone
            # end_time - Interval end timestamp with timezone

            return df
        except Exception as e:
            print(f"Error loading analysis file: {e}")
            import traceback
            traceback.print_exc()
            return None

    @staticmethod
    def load_ceph_df(results_dir, test_name, timing):
        json_file = Path(results_dir) / 'sysstat' / \
            test_name / f'ceph_df_{timing}.json'
        with open(json_file) as f:
            data = json.load(f)

        # JSON structure:
        # stats - Cluster-wide storage statistics
        #   total_bytes - Total raw storage capacity in bytes
        #   total_avail_bytes - Total available storage in bytes
        #   total_used_bytes - Total used storage in bytes (logical)
        #   total_used_raw_bytes - Total used storage in bytes (physical, including replication)
        #   total_used_raw_ratio - Percentage of raw storage used (0.0 to 1.0)
        #   num_osds - Number of OSDs in the cluster
        #   num_per_pool_osds - Number of OSDs per pool
        #   num_per_pool_omap_osds - Number of OSDs with OMAP data per pool
        #
        # stats_by_class - Storage statistics grouped by device class (e.g., ssd, hdd)
        #   Same fields as stats but per device class
        #
        # pools - Array of storage pool information
        #   name - Pool name (e.g., "default.rgw.buckets.data")
        #   id - Unique pool identifier
        #   stats - Pool-specific statistics
        #     stored - Logical data stored in bytes
        #     stored_data - User data stored in bytes
        #     stored_omap - OMAP (object map) data in bytes
        #     objects - Number of objects in the pool
        #     kb_used - Kilobytes used (for display)
        #     bytes_used - Total bytes used including metadata
        #     data_bytes_used - User data bytes only
        #     omap_bytes_used - OMAP data bytes
        #     percent_used - Percentage of pool quota used
        #     max_avail - Maximum available space for this pool in bytes
        #     quota_objects - Object count quota (0 = unlimited)
        #     quota_bytes - Byte quota (0 = unlimited)
        #     dirty - Number of dirty objects (not yet flushed)
        #     rd - Number of read operations
        #     rd_bytes - Bytes read
        #     wr - Number of write operations
        #     wr_bytes - Bytes written
        #     compress_bytes_used - Bytes used by compression
        #     compress_under_bytes - Bytes before compression
        #     stored_raw - Physical bytes stored (with replication)
        #     avail_raw - Raw available space for this pool

        return data

    @staticmethod
    def load_ceph_osd_df(results_dir, test_name, timing):
        json_file = Path(results_dir) / 'sysstat' / \
            test_name / f'ceph_osd_df_{timing}.json'
        with open(json_file) as f:
            data = json.load(f)

        # JSON structure:
        # nodes - Array of OSD information
        #   id - OSD numeric identifier
        #   device_class - Storage device type (ssd, hdd, nvme)
        #   name - OSD name (e.g., "osd.0")
        #   type - Daemon type (always "osd")
        #   type_id - Type identifier (0 for OSD)
        #   crush_weight - CRUSH map weight (typically device size in TB)
        #   depth - Position depth in CRUSH hierarchy
        #   pool_weights - Per-pool weight overrides
        #   reweight - OSD reweight factor (0.0 to 1.0, normally 1.0)
        #   kb - Total capacity in kilobytes
        #   kb_used - Total used space in kilobytes
        #   kb_used_data - User data in kilobytes
        #   kb_used_omap - OMAP data in kilobytes
        #   kb_used_meta - Metadata in kilobytes
        #   kb_avail - Available space in kilobytes
        #   utilization - Percentage of OSD capacity used (0.0 to 100.0)
        #   var - Variance from average cluster utilization (1.0 = average)
        #   pgs - Number of placement groups on this OSD
        #   status - OSD status ("up" or "down")
        #
        # stray - Array of OSDs not in CRUSH map (usually empty)
        #
        # summary - Cluster-wide OSD statistics
        #   total_kb - Total capacity across all OSDs in kilobytes
        #   total_kb_used - Total used space in kilobytes
        #   total_kb_used_data - Total user data in kilobytes
        #   total_kb_used_omap - Total OMAP data in kilobytes
        #   total_kb_used_meta - Total metadata in kilobytes
        #   total_kb_avail - Total available space in kilobytes
        #   average_utilization - Average utilization percentage across OSDs
        #   min_var - Minimum variance from average (best balanced OSD)
        #   max_var - Maximum variance from average (worst balanced OSD)
        #   dev - Standard deviation of utilization across OSDs

        return data

    @staticmethod
    def load_vmstat(results_dir, test_name, node):
        log_file = Path(results_dir) / 'sysstat' / \
            test_name / f'vmstat_{node}.log'

        data = []
        with open(log_file) as f:
            lines = f.readlines()

        for line in lines:
            parts = line.split()

            if len(parts) < 17:
                continue
            if parts[0] in ['procs', 'r']:  # Header row identifiers
                continue
            if 'memory' in line or 'swap' in line or 'cpu' in line:
                continue

            try:
                data.append({
                    'r': int(parts[0]),      # processes waiting for runtime
                    # processes in uninterruptible sleep
                    'b': int(parts[1]),
                    'swpd': int(parts[2]),   # virtual memory used
                    'free': int(parts[3]),   # idle memory
                    'buff': int(parts[4]),   # memory used as buffers
                    'cache': int(parts[5]),  # memory used as cache
                    'si': int(parts[6]),     # swap in
                    'so': int(parts[7]),     # swap out
                    'bi': int(parts[8]),     # blocks received from device
                    'bo': int(parts[9]),     # blocks sent to device
                    'in': int(parts[10]),    # interrupts per second
                    'cs': int(parts[11]),    # context switches per second
                    'us': int(parts[12]),    # user time
                    'sy': int(parts[13]),    # system time
                    'id': int(parts[14]),    # idle time
                    'wa': int(parts[15]),    # wait time
                })
            except (ValueError, IndexError):
                continue

        return pd.DataFrame(data)

    @staticmethod
    def load_network_stats(results_dir, test_name, node):
        log_file = Path(results_dir) / 'sysstat' / \
            test_name / f'net_{node}.log'

        data = []
        with open(log_file) as f:
            for line in f:
                if 'IFACE' in line or 'Linux' in line or 'Average' in line or 'lo' in line:
                    continue
                parts = line.split()
                iface = parts[1]
                if len(parts) >= 9 and iface == "eth0":
                    try:
                        # The other parts after index 5 are 0's so not included
                        data.append({
                            'rxpck_s': float(parts[2]),   # packets received/s
                            # packets transmitted/s
                            'txpck_s': float(parts[3]),
                            'rxkB_s': float(parts[4]),    # KB received/s
                            'txkB_s': float(parts[5]),    # KB transmitted/s
                        })
                    except (ValueError, IndexError):
                        continue

        return pd.DataFrame(data)

    @staticmethod
    def load_mpstat(results_dir, test_name, node):
        log_file = Path(results_dir) / 'sysstat' / \
            test_name / f'mpstat_{node}.log'

        data = []
        with open(log_file) as f:
            for line in f:
                # Skip header lines, empty lines, and system info
                if not line.strip():
                    continue
                if '%usr' in line or 'Linux' in line or 'Average' in line:
                    continue

                parts = line.split()

                # Aggregated stats
                cpu = parts[1]
                if cpu != "all" or len(parts) < 12:
                    continue

                # mpstat output has 12 columns:
                # time, cpu, %usr, %nice, %sys, %iowait, %irq, %soft, %steal, %guest, %gnice, %idle
                try:
                    data.append({
                        'usr': float(parts[2]),
                        'nice': float(parts[3]),
                        'sys': float(parts[4]),
                        'iowait': float(parts[5]),
                        'irq': float(parts[6]),
                        'soft': float(parts[7]),
                        'steal': float(parts[8]),
                        'guest': float(parts[9]),
                        'gnice': float(parts[10]),
                        'idle': float(parts[11])
                    })
                except (ValueError, IndexError):
                    continue

        return pd.DataFrame(data)

    @staticmethod
    def load_iostat(results_dir, test_name, node):
        log_file = Path(results_dir) / 'sysstat' / \
            test_name / f'iostat_{node}.log'

        data = []
        with open(log_file) as f:
            for line in f:
                line = line.strip()

                # Skip empty lines, system info, and avg-cpu sections
                if not line or 'Linux' in line or 'avg-cpu' in line or line.startswith('Device'):
                    continue

                parts = line.split()

                if len(parts) < 23:
                    continue
                # only keep vdb data. root disk is irrelevant
                device_name = parts[0]
                if device_name != 'vdb':
                    continue

                try:
                    data.append({
                        # Device name
                        'device': device_name,
                        # Read requests per second
                        'r_s': float(parts[1]),
                        # Kilobytes read per second
                        'rkB_s': float(parts[2]),
                        # Read requests merged per second (before being sent to device)
                        'rrqm_s': float(parts[3]),
                        # Percentage of read requests that were merged
                        'rrqm_pct': float(parts[4]),
                        # Average time (ms) for read requests (queue + service time)
                        'r_await': float(parts[5]),
                        # Average size (KB) of read requests
                        'rareq_sz': float(parts[6]),
                        # Write requests per second
                        'w_s': float(parts[7]),
                        # Kilobytes written per second
                        'wkB_s': float(parts[8]),
                        # Write requests merged per second (before being sent to device)
                        'wrqm_s': float(parts[9]),
                        # Percentage of write requests that were merged
                        'wrqm_pct': float(parts[10]),
                        # Average time (ms) for write requests (queue + service time)
                        'w_await': float(parts[11]),
                        # Average size (KB) of write requests
                        'wareq_sz': float(parts[12]),
                        # Discard requests per second
                        'd_s': float(parts[13]),
                        # Kilobytes discarded per second
                        'dkB_s': float(parts[14]),
                        # Discard requests merged per second
                        'drqm_s': float(parts[15]),
                        # Percentage of discard requests that were merged
                        'drqm_pct': float(parts[16]),
                        # Average time (ms) for discard requests
                        'd_await': float(parts[17]),
                        # Average size (KB) of discard requests
                        'dareq_sz': float(parts[18]),
                        # Flush requests per second (force data to disk)
                        'f_s': float(parts[19]),
                        # Average time (ms) for flush requests
                        'f_await': float(parts[20]),
                        # Average queue length (requests waiting + being serviced)
                        'aqu_sz': float(parts[21]),
                        # Device utilization percentage (time device was busy)
                        'util': float(parts[22])
                    })
                except (ValueError, IndexError):
                    pass

        return pd.DataFrame(data)
