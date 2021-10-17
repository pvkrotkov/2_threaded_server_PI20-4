import socket
import concurrent.futures
import tqdm


def scan_port(host, port, progress_bar, ports):
    sock = socket.socket()
    sock.settimeout(0.5)
    try:
        sock.connect((host, port))
        ports.append(port)
    except:
        pass 
    progress_bar.update()


host = input('Введите хост: ')
start_port = int(input('Введите минимальный порт: '))
end_port = int(input('Введите максимальный порт: '))
thread = int(input('Сколько потоков использовать для сканирования одновременно: '))

ports = []
progress_bar = tqdm.tqdm(total=end_port-start_port+1)

with concurrent.futures.ThreadPoolExecutor(thread) as executor:
    futures = []
    for port in range(start_port, end_port+1):
        future = executor.submit(scan_port, host, port, progress_bar, ports)
        futures.append(future)
    for future in futures:
        future.result()
progress_bar.close()
for port in ports:
    print(f'Порт {port} открыт!')
