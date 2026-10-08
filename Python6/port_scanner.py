import socket


class PortScanner:

    def scan(self, host):
        for port in range(1, 1025):
            sock = socket.socket()

            sock.settimeout(0.2)

            if sock.connect_ex((host, port)) == 0:
                print("Open:", port)

            sock.close()