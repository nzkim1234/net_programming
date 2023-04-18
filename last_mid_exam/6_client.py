from socket import *

port = 2500
BUFSIZE = 1024

sock = socket(AF_INET, SOCK_DGRAM)

while True:
    msg = input('Enter a message ')
    if msg == 'q':
        break
    time = 1
    count = 0
    while True:    
        sock.sendto(msg.encode(), ('localhost', port))
        sock.settimeout(time)
        try:
            data, addr = sock.recvfrom(BUFSIZE)
        except timeout:
            count += 1
            if count >= 4:
                break
        else:
            print("server says: ",data.decode())
            break

sock.close()