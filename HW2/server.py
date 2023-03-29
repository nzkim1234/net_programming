import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 9001))
s.listen(2)

while True:
	client, addr = s.accept()
	print('connection from ', addr)
	client.send(b'Hello ' + addr[0].encode())
	print(client.recv(1024).decode())
	client.send((20181509).to_bytes(8, 'big'))
	client.close()

