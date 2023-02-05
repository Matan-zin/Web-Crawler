import socks
import socket
import urllib.request as http


def create_connection(address, timeout = None, source_address = None):

    sock = socks.socksocket()
    sock.connect(address)

    return sock



class HttpService:

    
    def __init__(self, proxy_url, proxy_port):

        socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, proxy_url, proxy_port)
        socket.socket = socks.socksocket
        socket.create_connection = create_connection
    
    

    def get(self, url) -> str:

        req = http.Request(url)
        res = http.urlopen(req)
        
        return res.read().decode('utf-8')

