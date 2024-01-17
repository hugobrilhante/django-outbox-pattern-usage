#!/bin/bash

# Check if the number of arguments is valid
if [[ $# -lt 2 ]]; then
  echo "Usage: $0 <command> <profiles>"
  exit 1
fi

# Define the Docker Compose command
COMPOSE_CMD="docker compose"

# Define the command passed as an argument
CMD="$1"

# Define the profiles passed as arguments
PROFILES="${@:2}"

# Define the environment variable COMPOSE_PROFILES
export COMPOSE_PROFILES="${PROFILES// /,}"

# Check the passed command and execute the corresponding action
case $CMD in
  "build")
    $COMPOSE_CMD build
    ;;
  "up")
    $COMPOSE_CMD up -d --remove-orphans
    ;;
  "stop")
    $COMPOSE_CMD stop
    ;;
  "down")
    $COMPOSE_CMD down -v --remove-orphans
    ;;
  *)
    echo "Invalid command. Available options: build, up, stop, down."
    exit 1
    ;;
esac

# Clear the COMPOSE_PROFILES environment variable
unset COMPOSE_PROFILES
