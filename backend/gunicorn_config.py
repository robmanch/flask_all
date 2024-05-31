import multiprocessing

# Gunicorn configuration variables
bind = "0.0.0.0:5000"  # Bind to port 5000
workers = multiprocessing.cpu_count() * 2 + 1  # Number of worker processes

# SSL Configuration
certfile = "/app/flask.crt"  # Path to your SSL certificate file
keyfile = "/app/flask.key"   # Path to your SSL key file