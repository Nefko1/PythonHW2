import socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 1375))
while True:
    message = input('Сообщение: ')
    client.send(message.encode())
    response = client.recv(1024).decode()
    print(f'Сервер: {response}')
    if response.upper() == 'ББ':
        break
client.close()