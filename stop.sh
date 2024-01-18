#!/bin/bash

set -e

echo "Stopping  services..."

source run.sh down order stock payment > /dev/null 2>&1

docker volume prune -f > /dev/null 2>&1