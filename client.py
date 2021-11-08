import socket
sock= socket.socket()
sock.connect(('localhost', 9090))
print('Соединение с сервером обнаружено')
while True:
    msg = input()
    sock.send(msg.encode())
    print(f'Отправка серверу: {msg}')
    data = sock.recv(1024)
    print(f"Получено от сервера: {data.decode()}")
    if msg == "exit":
        sock.close()
        break
sock.close()
print('Соединено с сервером разорвано')