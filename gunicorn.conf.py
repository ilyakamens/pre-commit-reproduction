workers = 1
bind = "0.0.0.0:5000"
proc_name = "gunicorn"
pidfile = "/var/run/gunicorn.pid"
accesslog = "/dev/null"
errorlog = "-"
worker_class = "gevent"
debug = False
