export MESSAGE="${@}"
export DEBUG="0"
export FONT="6x12.bdf"
##export FONT="9x18B.bdf"
export FONT_D="/home/malonep/rpi-rgb-led-matrix/fonts"
export FONT_P="${FONT_D}/${FONT}"
if [ "${DEBUG}" == "1" ]; then
	echo "FONT  = ${FONT}"
	echo "FONT_D  = ${FONT_D}"
	echo "FONT_P  = ${FONT_P}"
fi
if [ -f "${FONT_P}" ]; then
sudo killall -q -r clock
sudo scrolling-text-example -f "${FONT_P}" --led-gpio-mapping=adafruit-hat --led-cols=64 --led-no-hardware-pulse -l2 -s4 "${MESSAGE}"
fi
