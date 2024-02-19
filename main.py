import socket
import sys
import time

def scan_ports(ip, start_port, end_port):
    open_ports = []
    try:
        for port in range(start_port, end_port + 1):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.1)

            result = sock.connect_ex((ip, port))

            if result == 0:
                open_ports.append(port)
            sock.close()
    except KeyboardInterrupt:
        print("Сканирование прервано пользователем.")
        sys.exit()
    except socket.gaierror:
        print("Не удалось разрешить адрес хоста.")
        sys.exit()
    except socket.error:
        print("Не удалось подключиться к серверу.")
        sys.exit()

    return open_ports

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Использование: python scanner.py <IP> <начальный порт> <конечный порт>")
        sys.exit()

    ip = sys.argv[1]
    start_port = int(sys.argv[2])
    end_port = int(sys.argv[3])

    if start_port < 0 or end_port > 65535:
        print("Порты должны быть в диапазоне от 0 до 65535.")
        sys.exit()

    print(f"Начало сканирования портов на {ip}...")
    start_time = time.time()
    open_ports = scan_ports(ip, start_port, end_port)
    end_time = time.time()
    print(f"Сканирование завершено за {end_time - start_time:.2f} секунд.")

    if open_ports:
        print("Открытые порты:")
        for port in open_ports:
            print(port)
    else:
        print("Нет открытых портов на сервере.")
