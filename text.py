#python2
import time
import sys
import os

sys.path.append(os.path.abspath(os.path.dirname(__file__) + './deps'))

sys.path.append(os.path.abspath(os.path.dirname(__file__) + './'))
from rgbmatrix import RGBMatrix, RGBMatrixOptions
from rgbmatrix import graphics
from . import RGBColor

# Set up RGB matrix options
options = RGBMatrixOptions()
options.rows = 32
options.cols = 64
options.chain_length = 2
options.parallel = 1
options.hardware_mapping = 'adafruit-hat'
matrix = RGBMatrix(options=options)

# Set up RGBColor object for text, background, and outline colors
color = RGBColor((255, 255, 255), (0, 0, 0), (0, 0, 0))

# Create graphics object and set font
font = graphics.Font()
font.LoadFont("../../../fonts/5x8.bdf")
text_graphics = graphics.Drawer(matrix)

# Set up two lines of text to display
line1 = "Hello world!"
line2 = "This is a test."

# Set text positions and draw text
x1 = 1
y1 = 9
x2 = 1
y2 = 19
text_graphics.SetFont(font)
text_graphics.SetTextColor(*color.get_text_color())
text_graphics.SetBackgroundColor(*color.get_bg_color())
text_graphics.SetTextWrap(False)

# Validate legibility of text and background colors
if not color.is_legible():
    sys.exit("Text color and background color do not have enough contrast to be legible.")

# Draw first line of text with outline
text_graphics.DrawText(x1, y1, color.get_outline_color(), line1)
text_graphics.DrawText(x1, y1, color.get_text_color(), line1)

# Draw second line of text with outline
text_graphics.DrawText(x2, y2, color.get_outline_color(), line2)
text_graphics.DrawText(x2, y2, color.get_text_color(), line2)

# Wait for 5 seconds before clearing display
time.sleep(5)
matrix.Clear()
