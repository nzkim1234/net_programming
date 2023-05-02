import socket
import random
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('localhost', 8888))
s.listen(2)

while True:
    client, addr = s.accept()
    print('Connection from ', addr)
    msg = client.recv(1024).decode()

    if msg == '1':
        temp = random.randint(1,50).to_bytes(4, 'big')
        print(temp)
        client.send(temp.to_bytes(4, 'big'))
    elif msg == '2':
        
        humid = str(random.randint(1,100))
        client.send(humid.encode())
    else:
        lumi = str(random.randint(1,150))
        client.send(lumi.encode())

client.close()