#!/usr/bin/env bash

set -x
timeout 30 docker stop drone
docker kill drone
docker rm drone

set -ex

docker run \
  --volume=/var/lib/drone:/data \
  --env=DRONE_GITHUB_CLIENT_ID=$DRONE_GITHUB_CLIENT_ID \
  --env=DRONE_GITHUB_CLIENT_SECRET=$DRONE_GITHUB_CLIENT_SECRET \
  --env=DRONE_RPC_SECRET=$DRONE_RPC_SECRET \
  --env=DRONE_SERVER_HOST=$DRONE_SERVER_HOST \
  --env=DRONE_SERVER_PROTO=$DRONE_SERVER_PROTO \
  --publish=80:80 \
  --publish=50443:443 \
  --restart=always \
  --detach=true \
  --name=drone \
  drone/drone:1

