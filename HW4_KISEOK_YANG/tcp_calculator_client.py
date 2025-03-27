import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('localhost', 9000))

print("TCP 계산기 클라이언트 실행됨. 예: 20 + 17")
print("q 입력 시 종료")

while True:
    msg = input("계산식 입력: ")
    sock.send(msg.encode())

    if msg.lower() == 'q':
        break

    data = sock.recv(1024)
    print("결과:", data.decode())

sock.close()
