import socket
from threading import Thread
from time import sleep


class T(Thread):
    ports = dict()

    # Инициализируем данные
    def __init__(self, n, start_port, end_port, step, address):
        Thread.__init__(self, name="t" + str(n))
        self.start_port = start_port
        self.end_port = end_port
        self.step = step
        self.address = address
        self.start()

    # Запускаем сканнер
    def run(self):
        for port in range(self.start_port, self.end_port + 1, self.step):
            sock = socket.socket()
            sock.settimeout(3)
            try:
                sock.connect((self.address, port))
                T.ports[port] = True
            except:
                T.ports[port] = False
            finally:
                sock.close()

    # Шкала прогресса

    @classmethod
    def progress(a, start, end):
        length = end - start + 1
        while True:
            a.print_progress(len(a.ports), length,
                             prefix="Прогресс", suffix="Выполнено", length=55)
            if len(a.ports) == length:
                break
            sleep(0.1)
        a.print_result(T.ports, start, end)

    @staticmethod
    def print_result(output, start, end):
        for i in range(start, end):
            print(f"Порт {i} {'открыт' if output[i] else 'закрыт'}")

    # Выводим шкалу прогресса

    @staticmethod
    def print_progress(iteration, total, prefix='', suffix='', decimals=1, length=100, fill='█'):
        percent = ("{0:." + str(decimals) + "f}").format(100 *
                                                         (iteration / float(total)))
        filledLength = int(length * iteration // total)
        bar = fill * filledLength + '-' * (length - filledLength)
        print(f'\r{prefix} |{bar}| {percent}% {suffix}', end="")
        if iteration == total:
            print()


# Функция для определения значений, введенных пользователем

def get_input():
    start_port = input("Введите начальный порт: ")
    start_port = 0 if start_port == "" else int(start_port)
    end_port = input("Введите конечный порт: ")
    end_port = 100 if end_port == "" else int(end_port)
    step = input("Введите шаг: ")
    step = 1 if step == "" else int(step)
    address = input("Введите адрес: ")
    address = "128.0.0.0" if address == "" else address
    return start_port, end_port, step, address

# Запускаем


def start_():
    start_port, end_port, step, address = get_input()
    threads = []
    T.port = start_port - 1
    for i in range(step):
        threads.append(T(i, start_port + i, end_port, step, address))
    thread = Thread(target=T.progress(start_port, end_port), name="result")
    thread.start()


if __name__ == '__main__':
    start_()
