import socks
import socket
import urllib.request as http


def create_connection(address, timeout = None, source_address = None):

    sock = socks.socksocket()

    sock.connect(address)

    return sock



class HttpService:

    
    def __init__(proxy_url, proxy_port):
        
        socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, proxy_url, proxy_port)
        
        socket.socket = socks.socksocket

        socket.create_connection = create_connection
    
    

    def get(url):

        req = http.Request(url)

        res = http.urlopen(req)

        print(str(res.read()))



http_service = HttpService('127.0.0.1', 8888)

http_service.get('http://strongerw2ise74v3duebgsvug4mehyhlpa7f6kfwnas7zofs3kov7yd.onion/pbebtdqcz')

