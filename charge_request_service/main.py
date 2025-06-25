
from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/request_charge', methods=['POST'])
def request_charge():
    resp = requests.post("http://load_balancer:7000/route")
    return resp.json(), resp.status_code

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6000)
