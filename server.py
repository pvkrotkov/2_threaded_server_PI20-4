import socket
import socket
import json
import hashlib
import pickle
from threading import Thread
from loger import Logfile

'''
def msgreciever(conn) ->str: #получения текстового сообщения с фиксированным заголовком
	msg_len = int(conn.recv(2), 10)
    return conn.recv(msg_len).decode()
def msgsending(conn, msg: str):   #отправкa сообщения с заголовком фиксированной длины
	msg = f"{len(msg):<{self.size}}" + msg
    conn.send(bytes(msg),"utf-8")
'''


sock = socket.socket()
sock.bind(('', 9090))
sock.listen(0)
conn, addr = sock.accept()
print(addr)

msg = ''
def checkPasswrd(passwd, userkey) -> bool:
		key = hashlib.md5(passwd.encode() + b'salt').hexdigest()
		return key == userkey

def generateHash(passwd) -> bytes:
		key = hashlib.md5(passwd.encode() + b'salt').hexdigest()
		return key
def check_port(port):
		global sock
		while True:
 			try:
 				sock.bind(('',port))
 				break
 			except:
				 port+=1
		print(f'Занял порт {port}')

def identification(conn,addr):
	try:
		open('users.json').close()
	except FileNotFoundError:
		open('users.json', 'a').close()
	with open('users.json', "r") as f:
		try:
			connectedUsers = json.load(f)
			name = connectedUsers[str(addr[0])]['name']
			conn.send(pickle.dumps(["pass","Введите свой пароль: "]))
			passwd = pickle.loads(conn.recv(1024))[1]
			conn.send(pickle.dumps(["accepted",f"Вошли успешно!"])) if checkPasswrd(passwd,connectedUsers[str(addr[0])]['password']) else identification(addr,conn)
		except:
			conn.send(pickle.dumps(["auth",f"Привет. Я тебя не знаю. Скажи мне свое имя: "]))
			name = pickle.loads(conn.recv(1024))[1]
			conn.send(pickle.dumps(["pass","Введите свой пароль: "]))
			passwd = generateHash(pickle.loads(conn.recv(1024))[1])
			conn.send(pickle.dumps(["accepted",f"Здравствуйте, {name}"]))
			with open("users.json", "w", encoding="utf-8") as f:
				json.dump({addr[0] : {'name': name, 'password': passwd} },f)


def listenClient(conn,addr):
	identification(conn,addr)
	while True:
		message = conn.recv(1024)
		if message:
				print(message.decode())
		else:
			conn.close()
			break

l = Logfile()
l.serverstart()
try:
	port=int(input("Ваш порт:"))
	if not 0 <= port <= 65535:
		raise ValueError
except ValueError:
		port = 9090

sock = socket.socket()
check_port(port)
sock.listen(5)
while True:
	data = conn.recv(1024)
	if not data:
		break
	msg += data.decode()
	conn.send(data)
	conn, addr = sock.accept()
	Thread(target=listenClient, args=(conn,addr)).start()

print(msg)

conn.close()
l.serverend()
