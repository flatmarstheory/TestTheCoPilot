# This code gets the IP address from a domain name
# The function name is get_ip_address_from_domain_name
# The variable name is domain

import socket


def get_ip_address_from_domain_name(domain):
    # get the IP address from the domain name
    ip_address = socket.gethostbyname(domain)
    # return the IP address
    return ip_address

print(get_ip_address_from_domain_name('www.google.com'))