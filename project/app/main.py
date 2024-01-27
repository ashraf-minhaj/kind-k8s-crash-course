# app.py
import logging
from flask import Flask
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
metrics = PrometheusMetrics(app, path='/metrics')

# Set the logging level to INFO
app.logger.setLevel(logging.INFO)

# Create a custom log format
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
handler = logging.StreamHandler()
handler.setFormatter(formatter)
app.logger.addHandler(handler)

@app.route('/')
def home():
    return "Hello, Kubernetes from kind!, version 1.2"

@app.route('/health')
def health():
    return "ok"

@app.route('/ready')
def ready():
    return "born ready"

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=8080)
