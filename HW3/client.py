from socket import *

s = socket(AF_INET, SOCK_STREAM)
s.connect(('localhost', 9001))

while True:
	msg = input('What should I calculate (q to quit): ')
	if msg == 'q':
		break
	s.send(msg.encode())
	print('Calculate result:', s.recv(1024).decode())

s.close()
