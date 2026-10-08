import socket


class MACLookup:

    def lookup(self, ip):
        try:
            print(socket.gethostbyaddr(ip))
        except Exception as e:
            print(e)