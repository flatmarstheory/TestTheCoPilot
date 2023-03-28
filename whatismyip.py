import urllib.request

def fetch_the_IP_address():
    # create the request for the IP address from a website
    request = urllib.request.Request('http://ip.42.pl/raw')
    # download the IP address from the website
    response = urllib.request.urlopen(request)
    # read the IP address from the website
    ip_address = response.read().decode('utf-8')
    # return the IP address
    return ip_address

print(fetch_the_IP_address())
