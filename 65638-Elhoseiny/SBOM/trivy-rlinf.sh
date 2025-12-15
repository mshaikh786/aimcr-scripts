docker run --rm \
    -v /var/run/docker.sock:/var/run/docker.sock \
    -v $PWD:/work \
    krccl/trivy:0.66.0 \
    trivy image --format spdx-json --output /work/result-rlinf.json \
    rlinf/rlinf:math-rlinf0.1-torch2.6.0-sglang0.4.6.post5-vllm0.8.5-megatron0.13.0-te2.1


