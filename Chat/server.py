# a simpele chatroom program to demonstrate chat functionality over a network with client-server model.

import threading
import socket

host = '127.0.0.1'
port = 59000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

clients = []
aliases = []

def broadcast(message):
    # to send message to all other clients
    for client in clients:
        client.send(message)

def handle_client(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)
        except:
            # clients that are causeing error or left the chat are removed from the list.
            index = clients.index(client)
            clients.remove(index)
            client.close()
            alias = aliases[index]
            alias.remove(alias)
            broadcast(f'{alias} has left the chatroom!'.encode('utf-8'))
            break

def recieve():
    while True:
        print('Server is running... ')
        client, addr = server.accept()
        print(f'Connection established with {str(addr)}')
        client.send("alias?".encode('utf-8'))
        alias = client.recv(1024) # 1024 is the max size of the message in bytes
        aliases.append(alias)
        clients.append(client)
        print(f'The alias of this client is {alias}'.encode('utf-8'))
        broadcast(f'{alias} has connected to the chatroom!'.encode('utf-8'))
        client.send(f'You are now connected!'.encode('utf-8'))

        thread = threading.Thread(target=handle_client, args=(client))
        thread.start()

if __name__ == '__main__':
    recieve()
