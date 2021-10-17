import socket


SERVER_ADDRESS = ('', 9090)


sock = socket.socket()
sock.connect(SERVER_ADDRESS)
while True:
    message = input()
    if message == 'exit':
        break
    sock.send(message.encode())
    data = sock.recv(1024)
    data_decode = data.decode()
    print(data_decode)

sock.close()