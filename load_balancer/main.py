
from flask import Flask, request, jsonify
import requests

app = Flask(__name__)
SUBSTATIONS = ['http://substation1:5000', 'http://substation2:5000']

def get_current_load(url):
    try:
        response = requests.get(f"{url.replace(':5000', ':8000')}/metrics")
        for line in response.text.split('\n'):
            if 'current_load' in line and not line.startswith('#'):
                return float(line.split(' ')[-1])
    except:
        return float('inf')
    return float('inf')

@app.route('/route', methods=['POST'])
def route_request():
    best_station = min(SUBSTATIONS, key=get_current_load)
    resp = requests.post(f"{best_station}/charge")
    return resp.json(), resp.status_code

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7000)
