# Dron-N Server

## Requirements

The whole infrastructure is built on top of [`docker`](https://www.docker.com/) and [`docker-compose`](https://docs.docker.com/compose/).

## Workflow Snippents

The application is managed using docker compose:

```console
# Start app
docker compose up --build
```

```console
# Stop app
docker compose down
```

```console
# Stop app and flush data
docker compose down
docker volume ls | grep influxdb-data | awk '{print $2}' | xargs docker volume rm
```

## Description

### Server

The central service of the applications is the server that handles HTTP requests and manages the database.
The server was designed to work over LAN, so it does not provide any security guarantees, other than input sanitization before updating the database.

Sample input for the server:

```json
{
  "reporter": "drone-N",
  "temp": 22.03,
  "humidity": 53.11,
  "heatIndex": 25.09
}
```

### InfluxDB

InfluxDB was chosen to store data because of its natural afinity to real-time data.

### Grafana

Grafana integrates well with InfluxDB and provides a nice interface to display measurements.
It is setup to load both the InfluxDB datasource and the Dro-N dashboard on start.

### Mock-Client

The mock-client is not a core part of the application, it rather is a tool to test the cluster in a confined environment.
Other than safe-guarding against bugs, it can be used for benchmarking.
# Thesis
# Thesis
