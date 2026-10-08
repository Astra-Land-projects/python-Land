import whois


class WhoisLookup:

    def lookup(self, domain):
        data = whois.whois(domain)

        print(data)