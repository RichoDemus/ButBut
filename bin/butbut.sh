#! /bin/sh
#
# chkconfig: 2345 90 10
# description:  solr-fs-indexer daemon

# . /etc/init.d/functions

# You will probably want to change only two following lines.
BASEDIR="/home/pi/applications/butbut/latest/"
USER="pi"

PROG="ButBut"
CMD="java -jar ${BASEDIR}/butbut.jar server ${BASEDIR}/config.yaml"
PIDFILE="${BASEDIR}/butbut.pid"
RETVAL=0

start () {
    echo -n $"Starting ${PROG}"
    if ( [ -f ${PIDFILE} ] )
    then
        echo "${PROG} is already running."
        #failure ; echo
        RETVAL=1
        return
    fi
    touch ${PIDFILE} ; chown ${USER} ${PIDFILE}
    java -jar ${BASEDIR}/butbut.jar server ${BASEDIR}/config.yaml >/dev/null 2>/dev/null &
    echo $! > ${PIDFILE}
}

stop () {
    echo $"Stopping ${PROG}"
    if ( [ ! -f ${PIDFILE} ] )
    then
        echo "${PROG} is not running."
        #failure ; echo
        RETVAL=1
        return
    fi
    cat ${PIDFILE} |xargs kill
    RETVAL=$?
    echo
    if [ $RETVAL -eq 0 ] ; then
        rm -f ${PIDFILE}
    fi
}

status () {
    if ( [ -f ${PIDFILE} ] )
    then
        echo "${PROG} is running."
	else
        echo "${PROG} is not running."
    fi
	echo
}

restart () {
    stop
    start
}


# See how we were called.
case "$1" in
  start)
    start
    ;;
  stop)
    stop
    ;;
  status)
    status
    ;;
  restart)
    restart
    ;;
  *)
    echo $"Usage: $0 {start|stop}"
    RETVAL=2
    ;;
esac

exit $RETVAL