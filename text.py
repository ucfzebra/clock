#!python3
import time
import sys
import os
from rgbmatrix import RGBMatrix, RGBMatrixOptions
from samplebase import SampleBase
from rgbmatrix import graphics
from rgbcolor.RGBColor import RGBColor

# Set up RGB matrix options
options = RGBMatrixOptions()
options.rows = 32
options.cols = 64
options.chain_length = 2
options.parallel = 1
options.hardware_mapping = 'adafruit-hat'
matrix = RGBMatrix(options=options)

# import random
sys.path.append(os.path.abspath(os.path.dirname(__file__) + './deps'))
sys.path.append(os.path.abspath(os.path.dirname(__file__) + './'))


class RunText(SampleBase):
    def __init__(self, *args, **kwargs):
        super(RunText, self).__init__(*args, **kwargs)
        self.parser.add_argument("-t", "--text",
                                 help="The text to scroll on the RGB \
                                    LED panel", default="Hello world!")

    def run(self):
        offscreen_canvas = self.matrix.CreateFrameCanvas()
        font = graphics.Font()
        font.LoadFont("../../../fonts/7x13.bdf")
        # Set up RGBColor object for text, background, and outline colors
        color = RGBColor()
        textColor = graphics.Color(*color.get_text_color)
        pos = offscreen_canvas.width
        my_text = self.args.text

        while True:
            offscreen_canvas.Clear()
            len = graphics.DrawText(offscreen_canvas, font, pos, 10,
                                    textColor, my_text)
            pos -= 1
            if (pos + len < 0):
                pos = offscreen_canvas.width

            time.sleep(0.05)
            offscreen_canvas = self.matrix.SwapOnVSync(offscreen_canvas)


# Main function
if __name__ == "__main__":
    run_text = RunText()
    if (not run_text.process()):
        run_text.print_help()
