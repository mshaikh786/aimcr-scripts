docker run --rm \
  -e TRIVY_TIMEOUT=60m \
  -v /var/run/docker.sock:/var/run/docker.sock \
  -v "$PWD":/work \
  -v "$HOME/.cache/trivy:/root/.cache/trivy" \
  krccl/trivy:0.66.0 \
  trivy image --parallel 0 \
  ghanem-stack:cu121-torch222 | tee stack.log
