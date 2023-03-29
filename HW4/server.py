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
		calc = data.decode()
		print(calc)
		if '+' in calc:
			calc = calc.split('+')
			result = int(calc[0]) + int(calc[1])

		elif '-' in calc:
			calc = calc.split('-')
			result = int(calc[0]) - int(calc[1])

		elif '*' in calc:
			calc = calc.split('*')
			result = int(calc[0]) * int(calc[1])

		else:
			calc = calc.split('/')
			result = round(int(calc[0]) / int(calc[1]), 1)
		print(result)
	try:	
		conn.send(str(result).encode())
	except:
		break
conn.close()


