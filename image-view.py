#!python3
import subprocess
import os


def main():
    # Kill any existing clock processes
    subprocess.call(["sudo", "killall", "-q", "-r", "clock"])

    # Start clock process with random text color and black background color
    gifs = []
    for file in os.path.listdir("./gifs"):
        if file.endswith('gif'):
            gifs.append(file)
    gifs_string = ""
    for i in gifs:
        gifs_string = ("%s %s" % (gifs_string, i))
    cmd = [
        "sudo",
        "led-image-viewer",
        "-C",
        "-t5",
        "-f",
        "-s",
        "--led-cols=64",
        "--led-gpio-mapping=adafruit-hat",
        "--led-no-hardware-pulse",
        "--led-daemon",
        gifs_string
    ]
    subprocess.call(cmd)
