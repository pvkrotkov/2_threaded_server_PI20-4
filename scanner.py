import socket
from threading import Thread
from time import sleep


class T(Thread):
    output = []

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
            sock.settimeout(0.05)
            try:
                sock.connect((self.address, port))
                T.output.append(True)
            except:
                T.output.append(False)
            finally:
                sock.close()

    # Шкала прогресса

    @classmethod
    def progress(a, start, end):
        length = end - start + 1
        while True:
            a.print_progress(len(a.output), length, prefix="Прогресс", suffix="Выполнено", length=55)
            if len(a.output) == length:
                break
            sleep(0.1)
        a.print_result(T.output, start)

    @staticmethod
    def print_result(output, start_port):
        for port, state in enumerate(output):
            print(f"Порт {port + start_port} {'открыт' if state else 'закрыт'}")

    # Выводим шкалу прогресса

    @staticmethod
    def print_progress(iteration, total, prefix='', suffix='', decimals=1, length=100, fill='█'):
        percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
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

def start():
    start_port, end_port, step, address = get_input()
    threads = []
    T.port = start_port - 1
    for i in range(step):
        threads.append(T(i, start_port + i, end_port, step, address))
    thread = Thread(target=T.progress(start_port, end_port), name="result")
    thread.start()


if __name__ == '__main__':
    start()
