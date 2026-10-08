import socket


class FileSender:

    def send(self, host, port, filename):
        client = socket.socket()

        client.connect((host, port))

        with open(filename, "rb") as file:
            client.sendall(file.read())

        client.close()

        print("File Sent.")