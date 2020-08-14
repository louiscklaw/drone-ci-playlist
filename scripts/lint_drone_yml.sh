#!/usr/bin/env bash

set -e

echo "linting drone yml files... "
for i in $(ls -1 */.drone.yml| sort); do
  echo 'linting yml file ' ${i}
  drone fmt $i
done
