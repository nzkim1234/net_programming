import struct
import binascii

class Udphdr:
    def __init__(self, src_port, dst_port, length, checksum):
        self.src_port = src_port
        self.dst_port = dst_port
        self.length = length
        self.checksum = checksum

    def pack_Udphdr(self):
        packed = b''
        packed += struct.pack('!HHHH', self.src_port, self.dst_port, self.length, self.checksum)
        return packed

def unpack_Udphdr(buffer):
    unpacked = struct.unpack('!HHHH', buffer)
    return unpacked

def getSrcPort(unpacked_Udpheader):
    return unpacked_Udpheader[0]

def getDstPort(unpacked_Udpheader):
    return unpacked_Udpheader[1]

def getLength(unpacked_Udpheader):
    return unpacked_Udpheader[2]

def getChecksum(unpacked_Udpheader):
    return unpacked_Udpheader[3]



udp = Udphdr(5555, 80, 1000, 0xFFFF)
packed_Udphdr = udp.pack_Udphdr() 
print(binascii.b2a_hex(packed_Udphdr))
unpacked_iphdr = unpack_Udphdr(packed_Udphdr) 
print(unpacked_iphdr)
print('Source Port:{} Destination Port:{} Length:{} Checksum:{}'.format(getSrcPort(unpacked_iphdr), getDstPort(unpacked_iphdr), getLength(unpacked_iphdr), getChecksum(unpacked_iphdr)))