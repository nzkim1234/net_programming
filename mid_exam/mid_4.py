import socket

ip = '220.69.189.125'
port = 443
hostname = socket.gethostbyaddr(ip)[0]
protocol = socket.getservbyport(port)
print(hostname)
print(protocol)
print(protocol + '://' + hostname)
print(socket.inet_aton(ip))