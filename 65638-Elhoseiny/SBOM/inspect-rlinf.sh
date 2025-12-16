docker run --rm \
  -e TRIVY_TIMEOUT=60m \
  -v /var/run/docker.sock:/var/run/docker.sock \
  -v "$PWD":/work \
  -v "$HOME/.cache/trivy:/root/.cache/trivy" \
  krccl/trivy:0.66.0 \
  trivy image --parallel 0 \
  rlinf/rlinf:agentic-rlinf0.1-torch2.6.0-openvla-openvlaoft-pi0 | tee rlinf.log

