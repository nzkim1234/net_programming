from socket import *
import sys

port = 9999
BUFSIZE = 1024

sock = socket(AF_INET, SOCK_STREAM)
sock.bind(('', port))
sock.listen(10)

mbox = {}

while True:
    conn, (remotehost, remoteport) = sock.accept()
    print('connected by', remotehost, remoteport)
    data = conn.recv(BUFSIZE)
    first_data = data.decode()
    print(first_data)

    if first_data == 'quit':
        conn.close()

    elif first_data == 'send':
        data = conn.recv(BUFSIZE)
        mboxID = data.decode()
        data = conn.recv(BUFSIZE)
        message = data.decode()
        if mboxID in mbox.keys():
            mbox[mboxID].append(message)
        else:
            mbox[mboxID] = []
            mbox[mboxID].append(message)
        print(mbox)
        conn.send(b'OK')

    else:
        data = conn.recv(BUFSIZE)
        mboxID = data.decode()

        if mboxID in mbox.keys() and len(mbox[mboxID]):
            conn.send(mbox[mboxID].pop(0).encode())
        else:
            conn.send('No messages'.encode())
        
        
        print(mbox)

conn.close()


