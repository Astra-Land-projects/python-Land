import socket


class FileReceiver:

    def receive(self, port):
        server = socket.socket()

        server.bind(("0.0.0.0", port))

        server.listen(1)

        client, _ = server.accept()

        with open("received.txt", "wb") as file:
            while True:
                data = client.recv(1024)

                if not data:
                    break

                file.write(data)

        print("Received.")