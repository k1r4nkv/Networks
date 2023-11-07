#a simple chatroom concept program to understand connections, client-server model over a network.

import threading
import socket

alias = input('Alias: ')
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(('127.0.0.1', 52000))

def clientRecieve():
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            if message == 'alias?':
                client.send(alias.encode('utf-8'))
            else:
                print(message)
        except:
            print("Error!")
            client.close()
            break

def send():
    while True:
        message = f'{alias}: {input(">")}'
        client.send(message.encode('utf-8'))

# a thread to recieve the message        
recieveThread = threading.Thread(target=clientRecieve)
recieveThread.start()

# a thread to send the message
sendThread = threading.Thread(target=send)
sendThread.start()
