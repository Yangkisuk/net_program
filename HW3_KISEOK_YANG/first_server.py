import socket
import struct  

s = socket.socket(socket.AF_INET, 
        socket.SOCK_STREAM)
s.bind(('', 9000))
s.listen(2)

while True:
    client, addr = s.accept()
    print('Connection from ', addr)
    client.send(b'Hello ' + addr[0].encode())
    name = client.recv(1024).decode()
    print(name)
    student_id = 20201508
    client.send(struct.pack('!I', student_id))
    client.close()
