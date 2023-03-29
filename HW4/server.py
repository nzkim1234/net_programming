from socket import *

port = 9001
BUFSIZE = 1024

sock = socket(AF_INET, SOCK_STREAM)
sock.bind(('', port))
sock.listen(1)
conn, (remotehost, remoteport) = sock.accept()
print('connected by', remotehost, remoteport)

while True:
	try:
		data = conn.recv(BUFSIZE)
	except:
		break
	else:
		if not data:
			break
		calc = data.decode().split()
		print(calc)
		if calc[1] == '+':
			result = int(calc[0]) + int(calc[2])
		elif calc[1] == '-':
			result = int(calc[0]) - int(calc[2])
		elif calc[1] == '*':
			result = int(calc[0]) * int(calc[2])
		else:
			result = round(int(calc[0]) / int(calc[2]), 1)
		print(result)
	try:	
		conn.send(str(result).encode())
	except:
		break
conn.close()


