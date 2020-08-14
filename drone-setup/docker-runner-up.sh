#!/usr/bin/env bash

set -x
docker pull drone/drone-runner-docker:1

timeout 10 docker stop drone-runner
docker kill drone-runner
docker rm drone-runner

set -ex


docker run -d \
  -v /var/run/docker.sock:/var/run/docker.sock \
  -e DRONE_RPC_PROTO=http \
  -e DRONE_RPC_HOST=home.louislabs.com:52102 \
  -e DRONE_RPC_SECRET=$DRONE_RPC_SECRET \
  -e DRONE_RUNNER_CAPACITY=3 \
  -e DRONE_RUNNER_NAME=${HOSTNAME} \
  -e DRONE_LOGS_TRACE=true \
  -p 3000:3000 \
  --restart always \
  --name drone-runner \
  drone/drone-runner-docker:1

# docker logs -f drone-runner
