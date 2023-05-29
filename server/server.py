import os
import sys
from flask import Flask, request

app = Flask(__name__)

@app.route('/data', methods=['POST'])
def handle_post_request():
    json_data = request.get_json()
    print(json_data, file=sys.stderr)

    return 'POST request received'

if __name__ == '__main__':
    SERVER_PORT=os.getenv('SERVER_PORT', '')
    if not SERVER_PORT:
        raise Exception('SERVER_PORT not set')
    
    app.run(host='0.0.0.0', port=SERVER_PORT, debug=False)
