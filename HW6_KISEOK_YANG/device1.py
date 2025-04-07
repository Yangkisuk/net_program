import socket
import random
import time

HOST = ''  
PORT = 8001  

def generate_sensor_data():
    temp = random.randint(0, 40)       
    humid = random.randint(0, 100)     
    illum = random.randint(70, 150)    
    return f"{temp},{humid},{illum}"

def main():
    server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_sock.bind((HOST, PORT))
    server_sock.listen(1)
    print(f"[디바이스1] 포트 {PORT}에서 대기 중...")

    conn, addr = server_sock.accept()
    print(f"[디바이스1] 연결됨: {addr}")

    while True:
        data = conn.recv(1024)
        if not data:
            break
        msg = data.decode()
        print(f"[디바이스1] 받은 메시지: {msg}")

        if msg == "Request":
            sensor_data = generate_sensor_data()
            print(f"[디바이스1] 전송할 센서 데이터: {sensor_data}")
            conn.send(sensor_data.encode())
        elif msg == "quit":
            print("[디바이스1] 종료 메시지 수신. 프로그램 종료.")
            break

    conn.close()
    server_sock.close()

if __name__ == "__main__":
    main()
