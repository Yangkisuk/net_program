from socket import *

BUFFSIZE = 1024
PORT = 2500

sock = socket(AF_INET, SOCK_DGRAM)

while True:
    msg = input('Enter the message("send mboxID message" or "receive mboxID"):')
    sock.sendto(msg.encode(), ('localhost', PORT))

    if msg == 'quit':
        break

    data, addr = sock.recvfrom(BUFFSIZE)
    print(data.decode())

sock.close()
