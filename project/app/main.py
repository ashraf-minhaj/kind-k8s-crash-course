# app.py
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Kubernetes from kind!"

@app.route('/health')
def health():
    return "ok"

@app.route('/ready')
def ready():
    return "born ready"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
