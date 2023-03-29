import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
addr = ('localhost', 9001)
sock.connect(addr)
msg = sock.recv(1024)
print(msg.decode())
sock.send(b'BoYoon Kim')
print(int.from_bytes(sock.recv(1024), 'big'))
sock.close()
