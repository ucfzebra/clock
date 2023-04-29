sudo ./text-scroller  --led-cols=64 \
                      --led-gpio-mapping=adafruit-hat \
                      -f ../fonts/9x15.bdf \
                      --led-slowdown-gpio=3 \
                      -s0 \
                      -C51,199,2555   
                      "$(date +%R)"