from influxdb import InfluxDBClient
from datetime import datetime


def initInfluxClient():
    influx_client = InfluxDBClient(host='influxdb', port=8086, username='root', password='root')

    database_name = 'meteoDB'
    if database_name not in influx_client.get_list_database():
        influx_client.create_database(database_name)

    influx_client.switch_database(database_name)

    return influx_client

def addDataToInflux(json_data, influx_client):
    required_fields = ['temp', 'humidity', 'heatIndex']

    if not all(field in json_data for field in required_fields):
        return False

    influx_metric = [
        {
            'measurement': 'DroneMetrics',
            'time': datetime.utcnow(),
            'fields': json_data
        }
    ]

    influx_client.write_points(influx_metric)

    return True
