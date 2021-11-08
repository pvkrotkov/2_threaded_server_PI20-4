import socket
import threading

class Thread(threading.Thread):
    n = 0
    def __init__(self, conn, addr):
        threading.Thread.__init__(self, name="t" + str(Thread.count))
        self.count = Thread.count
        Thread.count=Thread.count+1
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
         threads.append(Thread(conn, addr))