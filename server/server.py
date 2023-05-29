from flask import Flask, request
import json

app = Flask(__name__)

@app.route('/data', methods=['POST'])
def handle_post_request():
    json_data = request.get_json()
    print(json_data)

    return 'POST request received'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
