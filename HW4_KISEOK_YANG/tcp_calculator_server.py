import socket

def calculate(expression):
    try:
        expression = expression.replace(' ', '')

        if '+' in expression:
            a, b = expression.split('+')
            result = int(a) + int(b)
        elif '-' in expression:
            a, b = expression.split('-')
            result = int(a) - int(b)
        elif '*' in expression:
            a, b = expression.split('*')
            result = int(a) * int(b)
        elif '/' in expression:
            a, b = expression.split('/')
            result = round(int(a) / int(b), 1)  
        else:
            return "지원하지 않는 연산입니다."

        return str(result)
    except Exception as e:
        return "오류: 계산식 확인"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 9000))
s.listen(5)

print("서버가 실행 중입니다...")

while True:
    client, addr = s.accept()
    print("접속:", addr)

    while True:
        data = client.recv(1024)
        if not data:
            break

        expression = data.decode()
        if expression.lower() == 'q':
            break

        result = calculate(expression)
        client.send(result.encode())

    client.close()
