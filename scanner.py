import threading
import socket
from tqdm import tqdm
import random

def portscan(port):
    global r
    ports = []
    d = 101
    f = 1
    ip = input()
    for i in tqdm(range(f, d),desc="Port"):
        sock = socket.socket()
        sock.settimeout(0.5)
        try:
            connection = sock.connect((ip, i))
            ports.append(i)
            connection.close()
        except:
            #print(i)
            pass
    if len(ports) > 0:
        print(f'Список свободных портов {ports}')
        a = random.choice(ports)
        ports.remove(a)
        print(f'Порт {a} открыт')
    else:
        print('Нет свободных портов.')


s = 1  # Введите число s от 1 до 64 (это число умножается на 1024) для проверки портов. 1 = 1024, 64 = 65536
r = s * 100
print ("Запущено сканирование " + str(r) + " портов")
for element in range(s + 1):
    t = threading.Thread(target=portscan, kwargs={'port': element})
    t.start()
