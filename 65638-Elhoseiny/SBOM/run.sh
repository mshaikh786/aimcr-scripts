docker run --rm \
    -v /var/run/docker.sock:/var/run/docker.sock \
    -v $PWD:/work \
    krccl/trivy:0.66.0 \
    trivy image --format spdx-json --scanners vuln --output /work/result.json \
    roll-registry.cn-hangzhou.cr.aliyuncs.com/roll/pytorch:nvcr-24.05-py3-torch260-sglang046


