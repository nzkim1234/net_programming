from socket import *
import random

BUF_SIZE = 1024
LENGTH = 4

sock = socket(AF_INET, SOCK_STREAM)
sock.bind(('',7777))
sock.listen(10)
print('Device1 is running')

while True:
    conn, addr = sock.accept()
    msg = conn.recv(BUF_SIZE).decode()

    if msg == 'quit':
        conn.send(b'quit')
        break
    else:
        temp = random.randrange(0,40)
        humid = random.randrange(0,100)
        lilum = random.randrange(70,150)
        text = f"{temp} {humid} {lilum}"
        conn.send(text.encode())
        conn.close()

conn.close()