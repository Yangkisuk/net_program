import socket
import random
import time

HOST = ''
PORT = 8002  

def generate_health_data():
    heartbeat = random.randint(40, 140)
    steps = random.randint(2000, 6000)
    cal = random.randint(1000, 4000)
    return f"{heartbeat},{steps},{cal}"

def main():
    server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_sock.bind((HOST, PORT))
    server_sock.listen(1)
    print(f"[디바이스2] 포트 {PORT}에서 대기 중...")

    conn, addr = server_sock.accept()
    print(f"[디바이스2] 연결됨: {addr}")

    while True:
        data = conn.recv(1024)
        if not data:
            break
        msg = data.decode()
        print(f"[디바이스2] 받은 메시지: {msg}")

        if msg == "Request":
            health_data = generate_health_data()
            print(f"[디바이스2] 전송할 헬스 데이터: {health_data}")
            conn.send(health_data.encode())
        elif msg == "quit":
            print("[디바이스2] 종료 메시지 수신. 프로그램 종료.")
            break

    conn.close()
    server_sock.close()

if __name__ == "__main__":
    main()
