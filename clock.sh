export FONT="6x12.bdf"
##export FONT="9x18B.bdf"
export FONT_D="/home/malonep/rpi-rgb-led-matrix/fonts"
export FONT_P="${FONT_D}/${FONT}"
if [[ - e ${DEBUG} == 1 ]]; then
	echo "FONT  = ${FONT}"
	echo "FONT_D  = ${FONT_D}"
	echo "FONT_P  = ${FONT_P}"
fi
if [ -f "${FONT_P}" ]; then
 sudo killall -q -r clock
 sudo clock -f "${FONT_P}" \
           --led-cols=64 \
           --led-gpio-mapping=adafruit-hat \
           --led-no-hardware-pulse \
           --led-daemon \
             -d '%R' \
             -C0,0,200 \
#             -O0,0,200
fi
