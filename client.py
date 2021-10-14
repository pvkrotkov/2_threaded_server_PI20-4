import socket

def ser_ver():
    sock = socket.socket()
    sock.connect(('localhost', 9090))

    while True:
        message = input()
        if message == 'exit':
            break
        sock.send(message.encode())
        print(sock.recv(1024).decode())

    sock.close()
    
ser_ver()

#Делаем объявление сокета и подключаемся по порту к локальному хосту, на котором работает сервер.
#Далее производим отправление данных серверу, пока от пользователя не поступит команда "exit".
#После чего производим печать полученных данных и закрываем сокет.
