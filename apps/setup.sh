#!/usr/bin/env bash

VERSION="0.1.0"
ROOT_DIR="$(pwd)"

# Globals
echo "----------------------------------------------------------------"
echo "Setting up HomeServer version:${VERSION}!"
echo "Starting setup..."
echo "----------------------------------------------------------------"
echo "Shutting down active app instances"
echo "----------------------------------------------------------------"
docker-compose -f $ROOT_DIR/main.yaml down
docker-compose -f $ROOT_DIR/whoami/whoami.yaml down
docker network rm proxy

echo "----------------------------------------------------------------"
echo "Removing old app configurations"
rm $ROOT_DIR/main.yaml $ROOT_DIR/whoami/whoami.yaml $ROOT_DIR/traefik/traefik.yaml

echo "----------------------------------------------------------------"
echo "Adding new app configurations"
cp $ROOT_DIR/dist.main.yaml $ROOT_DIR/main.yaml
cp $ROOT_DIR/traefik/dist.traefik.yaml $ROOT_DIR/traefik/traefik.yaml
cp $ROOT_DIR/whoami/dist.whoami.yaml $ROOT_DIR/whoami/whoami.yaml
docker network create proxy

echo "----------------------------------------------------------------"
echo "Creating app instances"
echo "----------------------------------------------------------------"
docker-compose -f $ROOT_DIR/main.yaml up -d
docker-compose -f $ROOT_DIR/whoami/whoami.yaml up -d

echo "----------------------------------------------------------------"
echo "Setup script completed"
echo "----------------------------------------------------------------"
