from socket import *
import threading
import time

PORT = 3333
BUFSIZE = 1024
clients = []
lock = threading.Lock()

def broadcast(msg, sender_sock):
    with lock:
        for client in clients:
            if client != sender_sock:
                try:
                    client.send(msg)
                except:
                    clients.remove(client)

def handle_client(client_sock, addr):
    try:
        nickname = client_sock.recv(BUFSIZE).decode().strip()
        print(f"new client {addr}")
        print(f"{time.asctime()} {addr}: [{nickname}]")  # ← 원하는 로그 출력

        while True:
            data = client_sock.recv(BUFSIZE)
            if not data:
                break
            timestamp = time.asctime()
            print(f"{timestamp} {addr}: [{nickname}] {data.decode()}")  # 닉네임 포함 로그
            message = f"[{nickname}] {data.decode()}"
            broadcast(message.encode(), client_sock)
    except:
        pass
    finally:
        with lock:
            if client_sock in clients:
                clients.remove(client_sock)
        client_sock.close()

def main():
    server_sock = socket(AF_INET, SOCK_STREAM)
    server_sock.bind(('', PORT))
    server_sock.listen(5)
    print("Server Started")

    while True:
        client_sock, addr = server_sock.accept()
        with lock:
            clients.append(client_sock)
        th = threading.Thread(target=handle_client, args=(client_sock, addr))
        th.start()

if __name__ == "__main__":
    main()
