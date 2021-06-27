#!/bin/sh

# get the port from env var $PORT set randomly by heroku
if [ -z $PORT ]; then
  PORT=5555
fi
echo "running on port $PORT"
. /.venv/bin/activate
uwsgi --yaml app.yml