import socket
import time
import sys
from threading import Thread


PORT_AMOUNT = 1000 # сколько портов нужно проверить
THR_AMOUNT = 10 # количество потоков
threads = []
open_ports = []
address = input('Введите адрес для проверки портов: ')

# настройка прогресс бара
toolbar_width = THR_AMOUNT
sys.stdout.write("[%s]" % (" " * toolbar_width))
sys.stdout.flush()
sys.stdout.write("\b" * (toolbar_width+1))


def scan(address, ports):
    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        try:
            sock.connect((address, port))
            global open_ports
            open_ports.append(port)
        except:
            continue
        finally:
            sock.close()
    sys.stdout.write("-")
    time.sleep(0.001)
    sys.stdout.flush()

for i in range(1,THR_AMOUNT+1):
    infinum = PORT_AMOUNT*(i-1)//THR_AMOUNT # первый порт для потока №i
    suprenum = i*PORT_AMOUNT//THR_AMOUNT # последний порт для потока №i
    threads.append(Thread(target=scan, args=(address, [port for port in range(infinum, suprenum)])))

[t.start() for t in threads] # запуск всех потоков
[t.join() for t in threads] # дожидаемся завершения всех потоков
sys.stdout.write("\n")

print('Открытые порты: ', end='')
for port in sorted(open_ports):
    print(port, end=' ')

print(f'\nВсего: {len(open_ports)}.')
