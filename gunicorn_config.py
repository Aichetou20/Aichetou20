import multiprocessing

# Gunicorn configuration
bind = "0.0.0.0:8000"
workers = multiprocessing.cpu_count() * 2 + 1
threads = 2
worker_class = "gthread"
timeout = 120
keepalive = 5

# Logging
accesslog = "/var/log/gunicorn_access.log"
errorlog = "/var/log/gunicorn_error.log"
loglevel = "info"

# Process naming
proc_name = "INPC_gunicorn"

# SSL (if needed)
# keyfile = "/etc/ssl/private/your-key.pem"
# certfile = "/etc/ssl/certs/your-cert.pem"
