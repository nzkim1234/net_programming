import socket
import random

port = 2500
BUFSIZE = 1024

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('', port))

while True:
    msg, addr = sock.recvfrom(BUFSIZE)

    if random.randint(1, 10) <= 4:
        print("lost")
        continue
    print("Received: ", msg.decode())

    sock.sendto('ack'.encode(), addr)