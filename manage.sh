#!/bin/bash

SERVICE_NAME=$1
DJANGO_COMMAND=$2

docker compose run --rm "$SERVICE_NAME" python manage.py "$DJANGO_COMMAND" "${@:3}"

