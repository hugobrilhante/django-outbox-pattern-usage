#!/bin/bash

set -e

check_status() {
    status=$(curl -s -o /dev/null 2>&1 -w "%{http_code}" http://127.0.0.1:15672)

    if [ "$status" -eq 200 ]; then
        return 0
    else
        return 1
    fi
}

echo "Cleaning services..."

source run.sh down order stock payment > /dev/null 2>&1

echo "Running migrations..."

source manage.sh order migrate > /dev/null 2>&1
source manage.sh stock migrate > /dev/null 2>&1
source manage.sh payment migrate > /dev/null 2>&1

echo "Loading data..."

source manage.sh order loaddata order > /dev/null 2>&1
source manage.sh stock loaddata stock > /dev/null 2>&1
source manage.sh payment loaddata payment > /dev/null 2>&1

# Starting RabbitMQ to create the exchange
docker compose up -d rabbitmq > /dev/null 2>&1

while ! check_status; do
    echo "Creating saga exchange..."
    sleep 10
done

docker compose exec rabbitmq rabbitmqadmin declare exchange name=saga type=topic > /dev/null 2>&1

echo "Starting services..."

source run.sh up order stock payment > /dev/null 2>&1