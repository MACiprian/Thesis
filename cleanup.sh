#!/bin/bash

# stop the cluster and remove stored data
docker compose down
rm -rf grafana/grafana-storage influxdb/influxdb-storage
