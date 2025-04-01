from socket import *
import os

def get_mime_type(filename):
    if filename.endswith('.html'):
        return 'text/html'
    elif filename.endswith('.png'):
        return 'image/png'
    elif filename.endswith('.ico'):
        return 'image/x-icon'
    else:
        return None

server = socket()
server.bind(('', 80))  # 80 포트
server.listen(10)
print("웹 서버 실행 중...")

while True:
    client, addr = server.accept()
    data = client.recv(1024)
    msg = data.decode()
    request_line = msg.split('\r\n')[0]  # ex: GET /index.html HTTP/1.1
    print(f"요청: {request_line}")

    try:
        method, path, _ = request_line.split()
        filename = path[1:] if path != '/' else 'index.html'
        
        if not os.path.exists(filename):
            raise FileNotFoundError
        
        mimeType = get_mime_type(filename)
        if mimeType is None:
            raise FileNotFoundError
        
        # HTTP 헤더
        header = 'HTTP/1.1 200 OK\r\n'
        header += 'Content-Type: text/html; charset=utf-8\r\n'
        header += '\r\n'

        client.send(header.encode())

        # 파일 전송
        if mimeType.startswith('text'):
            with open(filename, 'r', encoding='utf-8') as f:
                client.send(f.read().encode('utf-8'))  # 한글 대응
        else:
            with open(filename, 'rb') as f:
                client.send(f.read())

    except:
        # Not Found
        response = 'HTTP/1.1 404 Not Found\r\n\r\n'
        response += '<html><head><title>Not Found</title></head>'
        response += '<body>Not Found</body></html>'
        client.send(response.encode('utf-8'))

    finally:
        client.close()
