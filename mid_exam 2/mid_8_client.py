from socket import *
port = 2500
BUFFSIZE = 1024
sock = socket(AF_INET, SOCK_DGRAM)

while True:
    
    msg = input('Enter a message: ')
    if msg == 'quit':
        break
    for i in range(4):
        sock.sendto(msg.encode(), ('localhost', port)) 
        sock.settimeout(2)
        try:
            data, addr = sock.recvfrom(BUFFSIZE) 
        except timeout:
            continue
        else:
            break
    print(data.decode())
sock.close()