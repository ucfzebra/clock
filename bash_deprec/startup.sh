#!/bin/bash
IP="$( hostname -I | sed -e 's/[ ].*$//')"
HOSTNAME="$( hostname -b ).local" 
echo ${HOSTNAME}
echo ${IP}
while true
do
  /bin/bash ~/clock/scrolling.sh "${IP} ${HOSTNAME}"
  /bin/bash ~/clock/clock.sh &
  sleep 60s
  sudo killall -r clock
done
