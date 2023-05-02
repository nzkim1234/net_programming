import socket
import random
import struct

class format:
    def __init__(self, sender, receiver, lumi, humi, temp, air, seq):
        self.sender = sender
        self.receiver = receiver
        self.lumi = lumi
        self.temp = temp
        self.air = air
        self.humi = humi
        self. seq = seq

    def pack_format(self):
        packed = b''
        packed += struct.pack('!HH', self.sender, self.receiver)
        packed += struct.pack('!BBBB', self.lumi, self.humi, self.temp, self.air)
        packed += struct.pack('!I', self.seq)
        return packed


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('localhost', 9999))
s.listen(2)
while True:
    client, addr = s.accept()
    print('Connection from ', addr)
    msg = client.recv(1024).decode()
    print(msg)
    sender = random.randint(1, 50000)
    receiver = random.randint(1, 50000)
    lumi = random.randint(1, 100)
    humi = random.randint(1, 100)
    temp = random.randint(1,100)
    air = random.randint(1, 100)
    seq = random.randint(1, 100000)
    print(sender, receiver, lumi, humi, temp, air, seq)
    send_format = format(sender, receiver, lumi, humi, temp, air, seq)
    packed_format = send_format.pack_format()
    client.send(packed_format)
    client.close()