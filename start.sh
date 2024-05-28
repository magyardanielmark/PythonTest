#!/bin/sh

# Start Nginx in the background
nginx -g 'daemon off;' &

# Start the Flask application
python3 app.py