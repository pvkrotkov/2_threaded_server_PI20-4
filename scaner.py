import time
from threading import Thread
import socket
from bar import ProgressBar
from validation import ip_validation, port_validation

DEFAULT_SERVER = "localhost"
DEFAULT_START_PORT = 1
DEFAULT_END_PORT = 19999


class PortScanner(Thread):

    def __init__(self, start_port: int = 1, end_port: int = 65535, host: str = DEFAULT_SERVER):
        """
        Порт сканер
        """

        super(PortScanner, self).__init__()

        self.start_port = start_port
        self.end_port = end_port + 1
        self.count = self.calculate_ports()
        self.host = host
        self.progress = 0
        self.progress_bar = ProgressBar(self.count)
        self.port_status = {}

    def run(self) -> None:
        """
        Старт потоков прогресс бара и сканера
        :return: None
        """

        progress_bar = Thread(target=self.update_bar)
        progress_bar.start()

        threads = []
        for i in range(self.start_port, self.end_port):
            threads.append(Thread(target=self.scanner, args=[i]))
        for tr in threads:
            tr.start()
        for tr in threads:
            tr.join()

    def calculate_ports(self) -> int:
        """
        Считает маскимальное кол-во портов
        :return: кол-во портов
        """

        return self.end_port - self.start_port

    def update_bar(self) -> None:
        """
        Обновляет состояние progress_bar
        :return: None
        """

        while self.progress < self.count:
            time.sleep(0.01)
            self.progress_bar.calculate(self.progress)

        # Сортировка по портам
        print()
        for key, value in sorted(self.port_status.items(), key=lambda x: x[0]):
            if value is True:
                print(f"Порт {key} открыт")

    def scanner(self, port: int) -> None:
        """
        Проверяем открыт ли порт
        :param port: порт
        :return: None
        """

        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            if self.host == "localhost" or self.host == "127.0.0.1":
                sock.settimeout(0.1)
            else:
                sock.settimeout(1)

        except OSError:
            scanner = Thread(target=self.scanner, args=(port,))
            scanner.start()
            return

        try:
            sock.connect((self.host, port))
            self.port_status[port] = True
        except OSError:
            self.port_status[port] = False
        finally:
            sock.close()
            self.progress += 1


if __name__ == '__main__':

    host_ = input("Введите ip сервера (enter для значения по умолчанию): ")
    if not ip_validation(host_):
        host_ = DEFAULT_SERVER
        print(f"Установили ip-адресс {host_} по умолчанию")

    start_port_ = input("Введите от какого порта сканим: ")
    if not port_validation(start_port_):
        start_port_ = DEFAULT_START_PORT
        print(f"Установили порт {start_port_} по умолчанию")

    end_port_ = input("Введите до какого порта сканим: ")
    if not port_validation(end_port_):
        end_port_ = DEFAULT_END_PORT
        print(f"Установили порт {end_port_} по умолчанию")

    print(f"\nДиапазон портов: от {start_port_} до {end_port_}")
    port_scanner = PortScanner(host=host_, start_port=int(start_port_), end_port=int(end_port_))
    port_scanner.start()