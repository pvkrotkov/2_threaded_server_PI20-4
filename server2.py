import socket
import threading

class Thr(threading.Thread):
    n = 0
    def __init__(self, conn, addr):
        threading.Thread.__init__(self, name="t" + str(Thr.n))
        self.n = Thr.n
        Thr.n=Thr.n+1
        self.conn = conn
        self.addr = addr
        self.start()
    def run(self):
        while True:
            data = self.conn.recv(1024)
            if not data:
                break
            print("Процесс", self.n, "Получено: ", data.decode())
            self.conn.send(data)

with socket.socket() as sock:
     threads = []
     sock.bind(('', 8083))
     sock.listen(0)
     while True:
         conn, addr = sock.accept()
         threads.append(Thr(conn, addr))