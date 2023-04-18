from socket import *

s = socket(AF_INET, SOCK_STREAM)
s.connect(('localhost', 9001))
BUFSIZE = 1024

while True:
    msg = input('Enter the message("send mboxId message" or "receive mboxId"): ')
    
    if msg == 'quit':
        print(msg)
        s.send(msg[0].encode())
        s.recv(BUFSIZE).decode()
        break
	
    msg = msg.split()

    if msg[0] == 'send':
        s.send(msg[0].encode())
        s.recv(BUFSIZE).decode()
        s.send(msg[1].encode())
        print(msg)
        s.recv(BUFSIZE).decode()
        message = ' '.join(msg[2::])
        s.send(message.encode())
    else:
        s.send(msg[0].encode())
        s.recv(BUFSIZE).decode()
        s.send(msg[1].encode())
        msg = s.recv(BUFSIZE).decode()
        print(msg)


s.close()
