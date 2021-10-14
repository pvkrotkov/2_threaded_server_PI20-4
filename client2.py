import socket
with socket.socket() as sock:
    sock.connect(('localhost', 8083))
    print('Соединение с сервером обнаружено')
    while True:
        line = input()
        sock.send(line.encode("utf-8"))
        print(f'Отправка серверу: {line}')
        data = sock.recv(1024)
        print(f"Получено от сервера: {data.decode('utf-8')}")
        if line == "exit":
            sock.close()
            break
print('Соединено с сервером разорвано')










   
