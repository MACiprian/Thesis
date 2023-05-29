import os
import sys
from flask import Flask, request
from influxClient import initInfluxClient, addDataToInflux

app = Flask(__name__)


@app.route('/data', methods=['POST'])
def handle_post_request():
    json_data = request.get_json()
    print(json_data, file=sys.stderr)

    try:
        status = addDataToInflux(json_data, influx_client)
    except Exception as e:
        print('Error adding data to influxdb: {}'.format(e), file=sys.stderr)
        return 'Error storing data', 500

    if status == False:
        return 'Mandatory fields missing', 400

    return 'OK'

if __name__ == '__main__':
    SERVER_PORT=os.getenv('SERVER_PORT', '')
    if not SERVER_PORT:
        raise Exception('SERVER_PORT not set')
    
    try:
        influx_client = initInfluxClient()
    except Exception as e:
        print('Error connecting to influxdb: {}'.format(e), file=sys.stderr)
        sys.exit(1)

    app.run(host='0.0.0.0', port=SERVER_PORT, debug=False)
