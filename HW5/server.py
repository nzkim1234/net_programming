from socket import *

s = socket()
s.bind(('', 80))
s.listen(10)

while True:
    c, addr = s.accept()

    data = c.recv(1024)
    msg = data.decode()
    req = msg.split('\r\n')
    request_url = req[0].split()[1][1::]

    print(request_url)
    print()

    if request_url == 'index.html':
        f = open(request_url, 'r', encoding='utf-8')
        mimeType = 'text/html'
        c.send('HTTP/1.1 200 OK\r\n'.encode())
        c.send(('Content-Type ' + mimeType + '\r\n').encode())
        c.send('\r\n'.encode())
        c.send(f.read().encode('euc-kr'))

    elif request_url == 'iot.png':
        f = open(request_url, 'rb')
        mimeType = 'image/png'
        c.send('HTTP/1.1 200 OK\r\n'.encode())
        c.send(('Content-Type: ' + mimeType + '\r\n').encode())
        c.send('\r\n'.encode())
        c.send(f.read())

    elif request_url == 'favicon.ico':
        f = open(request_url, 'rb')
        mimeType = 'image/x-icon'
        c.send('HTTP/1.1 200 OK\r\n'.encode())
        c.send(('Content-Type: ' + mimeType + '\r\n').encode())
        c.send('\r\n'.encode())
        c.send(f.read())

    else:
        c.send('HTTP/1.1 404 Not Found\r\n'.encode())
        c.send('\r\n'.encode())
        c.send('<HTML><HEAD><TITLE>Not Found</TITLE></HEAD>'.encode())
        c.send('<BODY>NOT FOUND</BODY></HTML>'.encode())

    c.close()