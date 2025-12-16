docker run --rm \
  -e TRIVY_TIMEOUT=60m \
  -v /var/run/docker.sock:/var/run/docker.sock \
  -v "$PWD":/work \
  -v "$HOME":/home  -v "$HOME/.cache/trivy:/root/.cache/trivy" \
  krccl/trivy:0.66.0 \
  trivy fs --parallel 0 \
  /home/miniconda3 | tee miniconda.log

