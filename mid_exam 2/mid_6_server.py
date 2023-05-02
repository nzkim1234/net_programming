import socket
import random
port = 7777
BUFFSIZE = 1024
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('localhost', port))

while True:
    msg, addr = sock.recvfrom(BUFFSIZE) 
    msg = msg.decode()
    print('Received: ', msg)  
    if msg == 'ping':
        if random.random() <= 0.6:
            print('sending pong')
            sock.sendto(b'pong', addr)
    else:
        print('not ping')