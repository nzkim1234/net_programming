import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
addr = ('localhost', 8888)
sock.connect(addr)

while True:    
    input_num = input("Enter a number(1, 2, 3): ")
    if input_num == '1':
        sock.send(input_num.encode())
    msg = sock.recv(1024)
    print(int.from_bytes(msg, 'big'))
sock.close()