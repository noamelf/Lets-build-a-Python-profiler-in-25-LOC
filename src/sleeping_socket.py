import socket
import time

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind(('localhost', 5000))
serversocket.listen()

print('Waiting for connections on port 5000...')
clientsocket, address = serversocket.accept()

print('Received a connection, going to sleep :)')
time.sleep(60)
