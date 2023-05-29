#!/bin/bash

# stop the cluster and remove stored data
docker compose down
docker volume ls | grep influxdb-data | awk '{print $2}' | xargs docker volume rm

