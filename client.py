import socket
from time import sleep
import sys
import pickle
from threading import Thread

sock = socket.socket()
sock.setblocking(1)
sock.connect(('10.38.165.12', 9090))
STATUS = None

#msg = input()
msg = "Hi!"
sock.send(msg.encode())

data = sock.recv(1024)
def recv():
        while True:
            try:
                global sock
                global STATUS
                data = sock.recv(1024)
                if not data: sys.exit(0)
                status = pickle.loads(data)
                STATUS = status

            except OSError:
                break

sock.close()
try:
    port=int(input("ваш порт:"))
    if not 0 <= port <= 65535:
        raise ValueError
except ValueError :
    port = 9090

print(data.decode())
sock = socket.socket()
sock.setblocking(True)
sock.connect(('localhost', port))
Thread(target=recv).start()
while True:
    if STATUS != None and STATUS == "exit":
        break
    elif STATUS:
        if STATUS[0] == "auth":
            name = pickle.dumps(["auth", input(STATUS[1])])
            sock.send(name)
            STATUS = None
        elif STATUS[0] == "pass":
            passwd = pickle.dumps(["pass", input(STATUS[1])])
            sock.send(passwd)
            STATUS = None
        elif STATUS[0] == "accepted":
            print(STATUS[1])
            STATUS = "typing"
        else:
            msg = input()
            if msg != "exit":
                sock.send(msg.encode())
            else:
                break
