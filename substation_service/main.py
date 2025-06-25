
from flask import Flask, request, jsonify
from prometheus_client import start_http_server, Gauge
import threading
import time

app = Flask(__name__)
current_load = Gauge('current_load', 'Current Load on Substation')

load = 0

@app.route('/charge', methods=['POST'])
def charge():
    global load
    load += 1
    current_load.set(load)
    threading.Thread(target=simulate_charging).start()
    return jsonify({"status": "Charging started"}), 200

def simulate_charging():
    global load
    time.sleep(10)
    load -= 1
    current_load.set(load)

if __name__ == '__main__':
    start_http_server(8000)
    app.run(host='0.0.0.0', port=5000)
