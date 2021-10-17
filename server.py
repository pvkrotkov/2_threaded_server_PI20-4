import socket
import threading


def processes_client(conn):
	while True:
		data = conn.recv(1024)
		if not data:
			break
		conn.send(data)


SERVER_ADDRESS = ('', 9090)


sock = socket.socket()
sock.bind(SERVER_ADDRESS)
sock.listen()
print('Начало прослушивания порта', SERVER_ADDRESS[1])

while True:
	conn, addr = sock.accept()
	thread = threading.Thread(target=processes_client, args=[conn])
	thread.start()
