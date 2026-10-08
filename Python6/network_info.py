import socket


class NetworkInfo:

    def show(self):
        hostname = socket.gethostname()
        ip = socket.gethostbyname(hostname)

        print("Hostname:", hostname)
        print("IP:", ip)