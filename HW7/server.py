from socket import *
import threading
import time

port = 2500
BUFSIZE = 1024

def echoTask(sock, remotehost, remoteport):
    out = False
    while True:
        data = sock.recv(BUFSIZE)
        # 'quit'을 수신하면 해당 클라이언트를 목록에서 삭제 
        if 'quit' in data.decode():
            if sock in clients:
                print(f'(\'{remotehost}\', {remoteport})', 'exited')
                clients.remove(sock)
                out = True

        print(f'{time.asctime()}(\'{remotehost}\', {remoteport}):{data.decode()}')
        # 모든 클라이언트에게 전송 
        for client in clients: 
            if client != sock:
                client.send(data)
        if out:
            break

    sock.close()


clients = []
sock = socket(AF_INET, SOCK_STREAM) 
sock.bind(('', port)) 
sock.listen(5)

while True:
    conn, (remotehost, remoteport) = sock.accept() 
    print(f'new client (\'{remotehost}\', {remoteport})')
    clients.append(conn)
    th = threading.Thread(target=echoTask, args=(conn, remotehost, remoteport)) 
    th.start()