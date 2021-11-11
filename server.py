import socket
import threading

def main():
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.bind(('localhost', 9091))
	sock.listen(5)
	while True:
	    threads = [threading.Thread(target=connect, args=[sock]) for _ in range(5)]
	    [thread.start() for thread in threads]
	    [thread.join() for thread in threads]

def connect(sock):
    while True:
        conn, addr = sock.accept()
        print(f'Новый пользователь: {addr}')
        if conn is not None:
            new_client(conn)

def new_client(conn):
    name = conn.recv(1024)
    name = name.decode()
    conn.send('Подключение установлено.'.encode())
    output(conn)

def output(conn):
    while True:
        data = conn.recv(1024)
        print(data.decode())

if __name__ == '__main__':
	main()
