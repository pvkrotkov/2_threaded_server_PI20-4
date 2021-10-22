import socket


# функция клиента

def main():
    with socket.socket() as sock:
        sock.connect(('localhost', 9090))
        print('Произошло соединение с сервером: ')
        while True:
            msg = input()
            # отправляем данные
            sock.send(msg.encode("utf-8"))
            print(f'Отправка данных серверу: {msg}')
            data = sock.recv(1024)
            print(f"Получено от сервера: {data.decode('utf-8')}")
            if msg == "exit":
                print("Отсоединение клиента")
                sock.close()
                break
    print('Соединено с сервером разорвано')


if __name__ == '__main__':
    main()