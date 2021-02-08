from flask import Flask, request
import os
import requests
import json

app = Flask(__name__)
url_to_post = os.getenv('BASECAMP_URL')

@app.route('/events', methods=['POST'])
def events():
    data = request.get_json()
    headers = {'Content-type': 'application/json'}
    requests.post(url_to_post, headers = headers, data = format_message(data))
    return '', 204

def format_message(payload):
    alert_triggered = payload['alert']['name']
    message_of_event = payload['event']['m']
    message = {"content" : "Alerta de {} con el mensaje {} fue activada".format(alert_triggered, message_of_event)}
    return json.dumps(message)

if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host='0.0.0.0', debug=True, port=80)