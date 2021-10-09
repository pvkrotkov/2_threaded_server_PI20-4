import socket


def main():
    with socket.socket() as sock:
        sock.connect(('localhost', 9090))
        print('Соединено с сервером')
        while True:
            line = input()
            sock.send(line.encode("utf-8"))
            print(f'Отправлено серверу: {line}')
            data = sock.recv(1024)
            print(f"Получено от сервера: {data.decode('utf-8')}")
            if line == "exit":
                sock.close()
                break
    print('Соединено с сервером разорвано')


if __name__ == '__main__':
    main()
