import socket


class ChatServer:

    def start(self):
        server = socket.socket()

        server.bind(("0.0.0.0", 5000))

        server.listen(1)

        print("Waiting...")

        client, addr = server.accept()

        print("Connected:", addr)

        while True:
            message = client.recv(1024).decode()

            if not message:
                break

            print("Client:", message)

            client.send(input("You: ").encode())