from socket import *
import threading

PORT = 3333
BUFSIZE = 1024

def receive(sock):
    while True:
        try:
            data = sock.recv(BUFSIZE)
            if not data:
                break
            print(data.decode())
        except:
            break

def main():
    sock = socket(AF_INET, SOCK_STREAM)
    sock.connect(('localhost', PORT))

    nickname = input("ID를 입력하세요: ")  
    sock.send(nickname.encode())  # 닉네임만 먼저 전송

    th = threading.Thread(target=receive, args=(sock,))
    th.daemon = True
    th.start()

    while True:
        msg = input()
        if msg.lower() == 'quit':
            sock.close()
            break
        sock.send(msg.encode())  # 메시지만 보냄

if __name__ == "__main__":
    main()
