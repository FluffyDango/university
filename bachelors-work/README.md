Commands not to forget

```bash
./s3bench -accessKey=minioadmin -accessSecret=minioadmin -bucket=loadgen -endpoint=http://node0:9000,http://node3:9000,http://node2:9000,http://node1:9000 -numClients=4 -numSamples=100 -objectNamePrefix=loadgen -objectSize=1024

nohup ~/test-suite.sh > ~/test-suite.log 2>&1 &

warp mixed \
  --host="node0:80" \
  --access-key="minioadmin" \
  --secret-key="minioadmin" \
  --obj.size="1KiB,1MiB" \
  --obj.randsize \
  --duration="2m" \
  --concurrent=10 \
  --benchdata="mixed-workload.csv.zst"

unzstd mixed-workload.csv.zst.json.zst
```

```bash
./s3bench -accessKey=minioadmin -accessSecret=minioadmin -bucket=loadgen -endpoint=http://node0 -numClients=4 -numSamples=100 -objectNamePrefix=loadgen -objectSize=1024
```
