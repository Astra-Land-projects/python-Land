import socket


class ChatClient:

    def start(self):
        client = socket.socket()

        client.connect(("127.0.0.1", 5000))

        while True:
            client.send(input("You: ").encode())

            message = client.recv(1024).decode()

            print("Server:", message)