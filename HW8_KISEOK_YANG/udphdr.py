import struct
import binascii

class Udphdr:
    def __init__(self, srcPort, dstPort, length, checksum):
        self.srcPort = srcPort
        self.dstPort = dstPort
        self.length = length
        self.checksum = checksum

    def pack_Udphdr(self):
        return struct.pack('!HHHH', self.srcPort, self.dstPort, self.length, self.checksum)

def unpack_Udphdr(buffer):
    return struct.unpack('!HHHH', buffer)

def getSrcPort(unpacked):
    return unpacked[0]

def getDstPort(unpacked):
    return unpacked[1]

def getLength(unpacked):
    return unpacked[2]

def getChecksum(unpacked):
    return unpacked[3]

udp = Udphdr(5555, 80, 1000, 0xFFFF)
packed = udp.pack_Udphdr()
print(binascii.b2a_hex(packed))  

unpacked = unpack_Udphdr(packed)
print(unpacked)  


print("Source Port:{} Destination Port:{} Length:{} Checksum:{}".format(
    getSrcPort(unpacked),
    getDstPort(unpacked),
    getLength(unpacked),
    getChecksum(unpacked)
))
