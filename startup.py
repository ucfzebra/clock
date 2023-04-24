#!python
import subprocess
import socket
import time
import sys

def get_ip_address():
    # Get IP address
    cmd = "hostname -I | sed -e 's/[ ].*$//'"
    process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
    output = process.communicate()[0]
    ip_address = output.strip()
    return ip_address

def get_hostname():
    # Get hostname
    hostname = socket.gethostname() + ".local"
    return hostname

def main():
    # Get IP address and hostname
    ip_address = get_ip_address()
    hostname = get_hostname()
    print(hostname)
    print(ip_address)
    
    # Start clock and scrolling text
    while True:
        subprocess.call(["python2", "~/clock/scrolling.py", "{} {}".format(ip_address, hostname)])
        subprocess.call(["python2", "~/clock/clock.py"])
        time.sleep(60)
        subprocess.call(["sudo", "killall", "-r", "clock"])

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        sys.stderr.write(str(e) + "\n")
        sys.exit(1)
