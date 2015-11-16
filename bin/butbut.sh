#! /bin/sh

#
# This is the start/stop-script for butbut
# it assumes that butbut.jar and config.yaml lies in BASEDIR
#

BASEDIR="/home/butbut/latest/"

PROG="ButBut"
CMD="java -jar ${BASEDIR}/butbut.jar server ${BASEDIR}/config.yaml"
PIDFILE="${BASEDIR}/butbut.pid"
RETVAL=0

start () {
    echo "Starting ${PROG}"
    if ( [ -f ${PIDFILE} ] )
    then
        echo "${PROG} is already running."
        #failure ; echo
        RETVAL=1
        return
    fi
    touch ${PIDFILE}
    java -jar ${BASEDIR}/butbut.jar server ${BASEDIR}/config.yaml >/dev/null 2>/dev/null &
    echo $! > ${PIDFILE}
}

stop () {
    echo "Stopping ${PROG}"
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