#!/bin/bash

if [ $# -ne 2 ]; then
    echo "Usage: $0 <service_name> <django_command>"
    exit 1
fi

SERVICE_NAME=$1
DJANGO_COMMAND=$2

docker compose run --rm $SERVICE_NAME python manage.py $DJANGO_COMMAND

