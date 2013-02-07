#!/bin/bash
set -e
LOGFILE=/var/log/gunicorn/iwantbetterfood.log
LOGDIR=$(dirname $LOGFILE)
NUM_WORKERS=3
# user/group to run as
USER=root
GROUP=root
PORT=9000
IP=127.0.0.1
cd /var/www/signmeup/server
source ../env/bin/activate
test -d $LOGDIR || mkdir -p $LOGDIR
exec /var/www/signmeup/env/bin/gunicorn_django -b $IP:$PORT -w $NUM_WORKERS \
--user=$USER --group=$GROUP --log-level=debug --log-file=$LOGFILE 2>>$LOGFILE