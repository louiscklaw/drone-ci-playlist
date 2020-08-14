#!/usr/bin/env bash

set -x
timeout 30 docker stop drone
docker kill drone
docker rm drone

set -ex

docker run \
  --volume=/var/lib/drone:/data \
  --env DRONE_GITHUB_CLIENT_ID=1a27c2983f103bdad722 \
  --env DRONE_GITHUB_CLIENT_SECRET=85e8e5f40135c997592edd2e474fec5561791b93 \
  --env DRONE_RPC_SECRET=$DRONE_RPC_SECRET \
  --env DRONE_SERVER_HOST=home.louislabs.com:52102 \
  --env DRONE_SERVER_PROTO=$DRONE_SERVER_PROTO \
  --env DRONE_USER_CREATE=username:louiscklaw,admin:true \
  --env DRONE_LOGS_TRACE=true \
  --env DRONE_LOGS_COLOR=true \
  --env DRONE_AGENTS_ENABLED=true \
  --publish=52102:80 \
  --publish=50443:443 \
  --publish=9000:9000 \
  --restart=always \
  --detach=true \
  --name=drone \
  drone/drone:1
