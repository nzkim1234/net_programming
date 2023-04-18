from socket import *

s = socket(AF_INET, SOCK_STREAM)

s.bind(('', 9001))
s.listen(10)

while True:
    c, addr = s.accept()
    data = c.recv(1024)
    print(1)
    msg = data.decode()
    req = msg.split('\r\n')
    print(2)
    
    s_2 = socket(AF_INET, SOCK_STREAM)
    s_2.connect((gethostbyname('www.daum.net'), 80))
    s_2.send("GET / HTTP/1.1\r\nHost: www.daum.net\r\n\r\n".encode("utf-8"))
    resp = s_2.recv(4096)
    s_2.close()
    print(3)
    c.send(resp)
    c.close()
    
