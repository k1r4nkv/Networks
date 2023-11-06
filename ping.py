import time
import subprocess

ip = input("Enter an IP address: ")

while True:
    pingCommand = f"ping {ip}"
    output = subprocess.run(pingCommand, capture_output=True)
    if output.returncode == 0:
        print(ip + " is up.")
    else:
        print(ip + " is down or maybe invalid")
    time.sleep(0.5)
    
