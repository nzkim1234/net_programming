import socket
import random

port = 2500
BUFFSIZE = 1024
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('', port))
mbox = {}
while True:
    msg, addr = sock.recvfrom(BUFFSIZE) 
    msg = msg.decode().split()
    
    if random.random() <= 0.1:
        sock.sendto(b'error', addr)
    else:
        if msg[0] == 'quit':
            break
        elif msg[0] == 'send':
            sock.sendto(b'OK', addr)
            full_msg = ' '.join(msg[2:])
            if msg[1] in mbox.keys():
                mbox[msg[1]].append(full_msg)
            else:
                mbox[msg[1]] = [full_msg]
        else:
            try: 
                msg[1] in mbox.keys()
                recv_msg = mbox[msg[1]].pop(0)
                sock.sendto(recv_msg.encode(), addr)
            except:
                sock.sendto(b'No messages', addr)
        
        print(mbox)