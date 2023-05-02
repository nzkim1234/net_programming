import socket
import time
port = 7777
BUFFSIZE = 1024
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
while True:
    msg = input('Insert ping: ')
    current_time = time.time()
    sock.settimeout(1)
    count = 0
    data = 0
    if msg == 'ping':
        while count <= 3:
            print(count)
            try:
                sock.sendto(msg.encode(), ('localhost', port)) 
                data, addr = sock.recvfrom(BUFFSIZE)   
                RTT = time.time() - current_time
            except socket.timeout:
                count += 1
            else:
                break

    if data != 0:
        print('Success (RTT: ' + str(RTT) + ')')
    else:
        print('fail')

sock.close()