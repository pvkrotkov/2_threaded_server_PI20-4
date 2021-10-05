import socket
from threading import Thread
import time
from progress.bar import IncrementalBar

N = 2**16 - 1

ports = []

def port_scanner(port_start, port_finish):
    #print(port_start, " ", port_finish)
    #addr = str(input("Введите IP-адресс пользователя: "))
    addr = "localhost"
    for port in range(port_start, port_finish + 1):
        sock = socket.socket()
        try:
            print(port)
            sock.connect((addr, port))
            ports.append(port)
            #print(port, "Добавлен")
            #print("Порт", port, "открыт")
        except:
            continue
        finally:
            sock.close()

def main():
    bar = IncrementalBar('Countdown', max = N)

    t1 = Thread(target=port_scanner, args=[0, 13107])
    t2 = Thread(target=port_scanner, args=[13108, 26214])
    t3 = Thread(target=port_scanner, args=[26215, 39321])
    t4 = Thread(target=port_scanner, args=[39322, 52428])
    t5 = Thread(target=port_scanner, args=[52429, 65535])

    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()

    for i in range(N):
        bar.next(n=5)
        time.sleep(1)

    bar.finish()

    t1.join()
    t2.join()
    t3.join()
    t4.join()
    t5.join()

    ports.sort()
    print(ports)

if __name__ == "__main__":
    main()