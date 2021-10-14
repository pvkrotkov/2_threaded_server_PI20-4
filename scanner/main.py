from scanner import P_Scanner


def ma_in():
    hostname = input('Введите имя хоста/IP-адрес: ')
    P_Scanner(hostname).scan_ports()


ma_in()
