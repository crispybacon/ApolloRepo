import httplib, ssl, urllib2
from IPython.display import HTML
from OpenSSL import SSL
#A simple HTTPS client implementation for use with REST API's
#Jesse Bacon
#6/5/2015

HOST = 'www.google.com'
PORT = '443'
METHOD = 'GET'
URL = '/'

def SSL_GET(HOST,PORT,METHOD,URL):
    context = ssl.SSLContext(SSL.SSLv23_METHOD)
    context.verify_mode = SSL.VERIFY_PEER
    #context.verify_mode = SSL.VERIFY_FAIL_IF_NO_PEER_CERT
    #context.verify_mode = SSL.VERIFY_NONE #For self signed certificates
    context.load_verify_locations("cacerts.pem.txt")
    j1 = httplib.HTTPSConnection(HOST, PORT, timeout=10, context=context)
    j1.request(METHOD, URL)
    rep = j1.getresponse()
    return rep.read()

def SSL_GET_WITH_HEADERS():
    pass

def SSL_GET_WITH_AGENT_STRING():
    pass

def encode_url(URL)
    pass


hosts = {}
headers = {}
agents = { 'mozilla_win': 'Mozilla/5.0 (Windows; Windows NT 6.1) AppleWebKit/534.57.2 (KHTML, like Gecko) Version/5.1.7 Safari/534.57.2', \
           'Mozilla_mac': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/600.6.3 (KHTML, like Gecko) Version/8.0.6 Safari/600.6.3', \
           'IE': 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)', \
           'IPhone': 'Mozilla/5.0 (iPhone; CPU iPhone OS 5_1 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9B179 Safari/7534.48.3', \
         }

#SSL_GET(HOST,PORT,METHOD,URL)