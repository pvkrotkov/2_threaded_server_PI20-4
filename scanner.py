import json
import pickle
import socket
import re
from time import sleep
from datetime import datetime
from dataclasses import dataclass, field
from threading import Thread

from progress.bar import IncrementalBar
from tqdm import tqdm


class Scanner(Thread):
    ports = []
    open_ports = []
    closed_ports = []
    percent = 0
    length = 0
    pbar = IncrementalBar('Countdown')

    def __init__(self, ip, initial_port, final_port):
        Thread.__init__(self)
        self.ip = ip
        self.initial_port = initial_port
        self.final_port = final_port
        Scanner.length = self.final_port - self.initial_port
        if not self.ip_validation(self.ip):
            print('Неправильный ip')
            exit()
        else:
            self.start()


    def start(self):
            self.is_free_port(self.initial_port)
            Scanner.print_progress(self.initial_port, self.final_port)

    def is_free_port(self, port):
        sock = socket.socket()
        sock.settimeout(3)
        try:
            sock.connect((self.ip, port))
        except:
            return Scanner.closed_ports.append(port)
        else:
            self.closed_port(port)
            return Scanner.open_ports.append(port)
        finally:
            sock.close()

    def ip_validation(self, ip):
        if ip == "" and ip != 'localhost':
            return False
        elif ip == 'localhost':
            return True
        else:
            try:
                octets = ip.split(".", 4)
                if len(octets) == 4:
                    for octet in octets:
                        octet = int(octet)
                        if 0 <= octet <= 255:
                            pass
                        else:
                            return False
                else:
                    return False
            except ValueError:
                return False
            return True

    def free_port(self, port):
        print(f"Порт {port} открыт")

    def closed_port(self, port):
        print(f"Порт {port} открыт")

    @classmethod
    def print_progress(Pbr, initial_port, final_port):
        length = final_port-initial_port
        Pbr.pbar.next()
        if length == 0:
            Pbr.pbar.finish()
            for i in Scanner.closed_ports:
                print(f"\n Порт {i} закрыт")
            for i in Scanner.open_ports:
                print(f"\n Порт {i} открыт")

def set_values():
    address = input("Введите ip: ")
    address = "localhost" if address == "" else address
    start_port = input("Введите начальный порт: ")
    start_port = 9000 if start_port == "" else int(start_port)
    end_port = input("Введите конечный порт: ")
    end_port = 9010 if end_port == "" else int(end_port)
    return start_port, end_port, address

def main():
    start_port, end_port, address = set_values()
    Scanner.pbar.max = end_port-start_port
    for i in range(end_port-start_port+1):
        thread = Thread(target=Scanner, args=(address, start_port+i, end_port))
        thread.start()

main()



