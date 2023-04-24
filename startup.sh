#!/bin/bash
IP="$( hostname -I | sed -e 's/[ ].*$//')"
HOSTNAME="$( hostname -b ).local" 
echo ${HOSTNAME}
echo ${IP}
while true
do
  sh ~/clock/scrolling.sh "${IP} ${HOSTNAME}"
  sh ~/clock/clock.sh &
  sleep 60s
  sudo killall -r clock
done
