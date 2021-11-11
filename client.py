import socket
import threading


def main():
    name = ''
    while not name:
        name = input('Ваше имя: ')

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(('localhost', 9091))
    t1 = threading.Thread(target=sending, args=[sock, name])
    t2 = threading.Thread(target=receiving)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    sock.close()


def sending(sock, name):
    sock.send(f'Клиент {name} присоединился'.encode())
    while True:
        mes = input(': ')
        sock.send(f'{name}: {mes}'.encode())
        if mes == 'exit':
            sock.close()
            break


def receiving():
    while True:
        try:
            data = sock.recv(1024)
            print(data.decode())
        except:
             print('Выход.')
             break


if __name__ == '__main__':
    main()
