#!python3
import subprocess
import sys
import random
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__) + './'))
sys.path.append(os.path.abspath(os.path.dirname(__file__) + './deps'))
from RGBColor import rgbcolor

# Set directory where font files are located
FONT_DIR = "/home/malonep/rpi-rgb-led-matrix/fonts"



def get_font_file():
    # Get list of font files
    font_files = [f for f in os.listdir(FONT_DIR) if f.endswith(".bdf")]
    if not font_files:
        sys.stderr.write("No font files found in directory {}\n".format(FONT_DIR))
        sys.exit(1)

    # Select random font file
    font_file = random.choice(font_files)
    
    # Verify font file has .bdf extension
    if not font_file.endswith(".bdf"):
        sys.stderr.write("Selected font file {} does not have a .bdf extension\n".format(font_file))
        sys.exit(1)
        
    return "{}/{}".format(FONT_DIR, font_file)

def main():
    # Kill any existing clock processes
    subprocess.call(["sudo", "killall", "-q", "-r", "clock"])

    # Create RGBColor object and randomize text color
    text_color = rgbcolor()
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
        "-C{},{},{}".format(*text_color.get_text_color()),
        "-B0,0,0"
    ]
    subprocess.call(cmd)

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        sys.stderr.write(str(e) + "\n")
        sys.exit(1)
