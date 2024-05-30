from flask import Flask, jsonify
from prometheus_client import make_wsgi_app, Counter, Histogram
from werkzeug.middleware.dispatcher import DispatcherMiddleware
import time

app = Flask(__name__)

# Prometheus WSGI middleware
app.wsgi_app = DispatcherMiddleware(app.wsgi_app, {
    '/metrics': make_wsgi_app()
})

# Prometheus metrics
REQUEST_COUNT = Counter(
    'app_request_count',
    'Application Request Count',
    ['method', 'endpoint', 'http_status']
)
REQUEST_LATENCY = Histogram(
    'app_request_latency_seconds',
    'Application Request Latency',
    ['method', 'endpoint']
)

# Flask route
@app.route('/')
def hello():
    start_time = time.time()
    REQUEST_COUNT.labels('GET', '/', 200).inc()  # Increment request counter
    response = jsonify(message='Hello, world!')
    REQUEST_LATENCY.labels('GET', '/').observe(time.time() - start_time)  # Observe latency
    return response

# Run the app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)