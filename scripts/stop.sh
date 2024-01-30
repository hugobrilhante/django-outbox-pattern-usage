#!/bin/bash

set -e

echo "Stopping  services..."

source scripts/run.sh down order stock payment rabbitmq kong kong-db > /dev/null 2>&1

docker volume prune -f > /dev/null 2>&1