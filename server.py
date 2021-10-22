import socket
import threading


# главный класс сервера

class T(threading.Thread):
    n = 0
    def __init__(self, conn, addr):
        threading.Thread.__init__(self, name="t" + str(T.n))
        self.n = T.n
        T.n += 1
        self.conn = conn
        self.addr = addr

        self.start()

    def run(self):
        while True:
            data = self.conn.recv(1024)
            if not data:
                print('Данные не корректны')
                break
            print("Процесс", self.n, "Получены: ", data.decode())
            self.conn.send(data)

def main():
    with socket.socket() as sock:
        threads = []
        sock.bind(('', 9090))
        sock.listen(0)
        while True:
            conn, addr = sock.accept()
            threads.append(T(conn, addr))


if __name__ == '__main__':
    main()