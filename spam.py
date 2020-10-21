from dnspython import resolver

# try:
#     mx_record = resolver.query('gmail.com', 'MX')
#     exchanges = [exchange.to_text().split() for exchange in mx_record]
# except (resolver.NoAnswer, resolver.NXDOMAIN, resolver.NoNameservers):
#     exchanges = []