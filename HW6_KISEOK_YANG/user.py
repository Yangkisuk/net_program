import socket
import time

DEVICE1_PORT = 8001
DEVICE2_PORT = 8002
HOST = 'localhost'
DATA_FILE = 'data.txt'

def connect_to_device(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((HOST, port))
    return sock

def get_timestamp():
    return time.ctime(time.time())

def main():
    d1 = connect_to_device(DEVICE1_PORT)
    d2 = connect_to_device(DEVICE2_PORT)
    print("[사용자] 디바이스 1, 2 연결 완료")

    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        while True:
            cmd = input("입력 (1: 디바이스1, 2: 디바이스2, quit: 종료): ")
            if cmd == '1':
                d1.send(b"Request")
                data = d1.recv(1024).decode()
                print(f"[사용자] 디바이스1 데이터 수신: {data}")
                log = f"{get_timestamp()}: Device1: Temp={data.split(',')[0]}, Humid={data.split(',')[1]}, Iilum={data.split(',')[2]}"
                f.write(log + '\n')
            elif cmd == '2':
                d2.send(b"Request")
                data = d2.recv(1024).decode()
                print(f"[사용자] 디바이스2 데이터 수신: {data}")
                log = f"{get_timestamp()}: Device2: Heartbeat={data.split(',')[0]}, Steps={data.split(',')[1]}, Cal={data.split(',')[2]}"
                f.write(log + '\n')
            elif cmd == 'quit':
                d1.send(b"quit")
                d2.send(b"quit")
                print("[사용자] 종료 메시지를 디바이스에 전송했습니다.")
                break
            else:
                print("올바른 명령어를 입력해주세요.")

    d1.close()
    d2.close()
    print("[사용자] 연결 종료 완료.")

if __name__ == "__main__":
    main()
