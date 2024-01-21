#!/bin/bash

set -e

echo "Stopping  services..."

source run.sh down order stock payment rabbitmq kong kong-db > /dev/null 2>&1

docker volume prune -f > /dev/null 2>&1

rm -rf order/logs/*
rm -rf stock/logs/*
rm -rf payment/logs/*