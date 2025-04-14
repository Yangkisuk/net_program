from socket import *

BUFFSIZE = 1024
PORT = 2500

mailbox = {}  # {mboxID: [messages]}

sock = socket(AF_INET, SOCK_DGRAM)
sock.bind(('', PORT))
print('📩 UDP 메시지 서버 실행 중...')

while True:
    data, addr = sock.recvfrom(BUFFSIZE)
    msg = data.decode().strip()

    if msg == 'quit':
        print('서버 종료 명령 수신')
        break

    elif msg.startswith('send '):
        try:
            _, mboxID, message = msg.split(' ', 2)
            if mboxID not in mailbox:
                mailbox[mboxID] = []
            mailbox[mboxID].append(message)
            sock.sendto(b'OK', addr)
        except:
            sock.sendto(b'Invalid send format', addr)

    elif msg.startswith('receive '):
        try:
            _, mboxID = msg.split(' ', 1)
            if mboxID in mailbox and mailbox[mboxID]:
                message = mailbox[mboxID].pop(0)
                sock.sendto(message.encode(), addr)
            else:
                sock.sendto(b'No messages', addr)
        except:
            sock.sendto(b'Invalid receive format', addr)

sock.close()
