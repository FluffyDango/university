#/bin/bash

# Using "minioadmin" for ceph to keep consistency
sudo radosgw-admin user create \
  --uid=minioadmin \
  --display-name="Admin" \
  --access-key=minioadmin \
  --secret-key=minioadmin
