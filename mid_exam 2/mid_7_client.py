import socket
import struct

def unpack_format(buffer):
    unpacked = struct.unpack('!HHBBBBI', buffer[:12]) 
    return unpacked
def getsender(unpacked_format): 
    return unpacked_format[0]
def getreceiver(unpacked_format): 
    return unpacked_format[1]
def getlumi(unpacked_format): 
    return unpacked_format[2]
def gethumi(unpacked_format): 
    return unpacked_format[3]
def gettemp(unpacked_format): 
    return unpacked_format[4]
def getair(unpacked_format): 
    return unpacked_format[5]
def getseq(unpacked_format): 
    return unpacked_format[6]


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
addr = ('localhost', 9999)
sock.connect(addr)
sock.send(b'Hello')
msg = unpack_format(sock.recv(1024))
print(f'Sender:{getsender(msg)}, Receiver:{getreceiver(msg)}, Lumi:{getlumi(msg)}, Humi{gethumi(msg)}, Temp:{gettemp(msg)}, Air: {getair(msg)}, Seq:{getseq(msg)}')
sock.close()