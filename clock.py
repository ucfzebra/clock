#!python3
import subprocess
import sys
import random
import os
import argparse
from rgbcolor.RGBColor import RGBColor
sys.path.append(os.path.abspath(os.path.dirname(__file__) + './'))
# sy1s.path.append(os.path.abspath(os.path.dirname(__file__) + './deps'))


# Set directory where font files are located
FONT_DIR = "/home/malonep/clock/fonts"


def get_font_file():
    # Get list of font files
    font_files = [f for f in os.listdir(FONT_DIR) if f.endswith(".bdf")]
    if not font_files:
        sys.stderr.write("No font files found in directory \
                         {}\n".format(FONT_DIR))
        sys.exit(1)

    # Select random font file
    font_file = random.choice(font_files)

    # Verify font file has .bdf extension
    if not font_file.endswith(".bdf"):
        sys.stderr.write("Selected font file {} \
                         does not have a .bdf extension\n".format(font_file))
        sys.exit(1)

    return "{}/{}".format(FONT_DIR, font_file)


def main():
    # Kill any existing clock processes
    subprocess.call(["sudo", "killall", "-q", "-r", "clock"])
    args = parse_arguments()
    # Create RGBColor object and randomize text color
    text_color = RGBColor()
    if args._get_args is None:
        text_color.randomize()
    # Create RGBColor object and randomize text color
    text_color = RGBColor()
    text_color.randomize()
    while not text_color.is_legible:
        text_color.randomize()
    # Start clock process with random text color and black background color
    font_file = get_font_file()
    cmd = [
        "sudo",
        "clock",
        "-f",
        font_file,
        "--led-cols=64",
        "--led-gpio-mapping=adafruit-hat",
        "--led-no-hardware-pulse",
        "--led-daemon",
        "-d", "%R",
        "-d", "%a %d/%m"
        "-C{},{},{}".format(*text_color.get_text_color())
        #"-B{},{},{}".format(*text_color.get_bg_color())

    ]
    subprocess.call(cmd)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        sys.stderr.write(str(e) + "\n")
        sys.exit(1)
