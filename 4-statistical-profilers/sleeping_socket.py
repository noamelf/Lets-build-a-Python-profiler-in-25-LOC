import socket
import time

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind(('localhost', 5000))
serversocket.listen()

clientsocket, address = serversocket.accept()
print('Received a connection, going to sleep :)')
time.sleep(60)
