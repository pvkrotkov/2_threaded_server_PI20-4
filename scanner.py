import socket
from threading import Thread
from time import sleep


class T(Thread):
    output = []

    def __init__(self, n, start_port, end_port, step, address):
        Thread.__init__(self, name="t" + str(n))
        self.start_port = start_port
        self.end_port = end_port
        self.step = step
        self.address = address
        self.start()

    def run(self):
        for port in range(self.start_port, self.end_port + 1, self.step):
            sock = socket.socket()
            try:
                sock.connect((self.address, port))
                T.output.append(True)
            except:
                T.output.append(False)
            finally:
                sock.close()

    @staticmethod
    def print_result(output, start_port):
        for port, state in enumerate(output):
            print(f"Порт {port + start_port} {'открыт' if state else 'закрыт'}")

    @staticmethod
    def print_progress_bar(iteration, total, prefix='', suffix='', decimals=1, length=100, fill='█'):
        percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
        filledLength = int(length * iteration // total)
        bar = fill * filledLength + '-' * (length - filledLength)
        print(f'\r{prefix} |{bar}| {percent}% {suffix}', end="")
        if iteration == total:
            print()

    @classmethod
    def progress_bar(cls, start, end):
        length = end - start + 1
        while True:
            cls.print_progress_bar(len(cls.output), length, prefix="Progress", suffix="Complete", length=50)
            if len(cls.output) == length:
                break
            sleep(0.1)
        cls.print_result(T.output, start)


def get_input():
    start_port = input("Enter start port: ")
    start_port = 2000 if start_port == "" else int(start_port)
    end_port = input("Enter end port: ")
    end_port = 2098 if end_port == "" else int(end_port)
    step = input("Enter step (= number of threads): ")
    step = 3 if step == "" else int(step)
    address = input("Enter address: ")
    address = "127.0.0.1" if address == "" else address
    return start_port, end_port, step, address


def main():
    start_port, end_port, step, address = get_input()
    list_of_threads = []
    T.port = start_port - 1
    for i in range(step):
        list_of_threads.append(T(i, start_port + i, end_port, step, address))
    thread = Thread(target=T.progress_bar(start_port, end_port), name="result")
    thread.start()


if __name__ == '__main__':
    main()
