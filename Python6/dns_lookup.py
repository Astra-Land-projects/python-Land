import socket


class DNSLookup:

    def lookup(self, domain):
        print(socket.gethostbyname(domain))