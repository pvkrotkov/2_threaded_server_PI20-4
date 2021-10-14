import socket
from concurrent.futures import ThreadPoolExecutor
from threading import RLock

from bar import P_Bar


class P_Scanner:

    PORTS_COUNT = 2 ** 16

    def __init__(self, host): #Хост, который мы хотим отсканировать.
        self._host = host
        self._progress_bar = ProgressBar(self.PORTS_COUNT, 'Выполнено')

    def scan_ports(self, threads_count=None): # Сканирует порты: добавляет в пул на обработку потоки со всем портами.threads_count: Максимальное кол-во потоков.
        self._progress_bar.print()
        with ThreadPoolExecutor(threads_count) as executor:    
            lock = RLock()
            for port in range(self.PORTS_COUNT):
                executor.submit(self._scan_port, port, lock)

    def info(self, message): #Корректно печатает сообщение в терминал при использовании бара. message: Строка, которую нужно распечатать.
        print(message,
              end=(' ' * (len(self._progress_bar) - len(message)) + '\n'))

    def _scan_port(self, port, lock):
        with socket.socket() as sock:                       
            try:
                sock.connect((self._host, port))                         
            except socket.error:
                pass
            else:
                with lock:
                    self.info(f'Порт {port} открыт')
            finally:
                with lock:
                    self._progress_bar.update()
                    
       # Сканирует один порт.
       # port: Порт.
       # lock: блокировка всех потоков. Используется, чтобы корректно напечатать бар и информацию об открытом порте.
