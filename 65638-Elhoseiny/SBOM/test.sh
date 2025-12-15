docker run --rm \
  -e TRIVY_TIMEOUT=10m \
  -e TRIVY_SKIP_DB_UPDATE=true \
  -v /var/run/docker.sock:/var/run/docker.sock \
  -v "$PWD":/work \
  aquasec/trivy:0.66.0 \
    image \
    --skip-db-update \
    --format spdx-json \
    --output /work/result-alpine.json \
    alpine:3.18

