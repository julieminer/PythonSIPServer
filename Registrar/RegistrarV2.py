import socket
import Messages
import threading

ProxyListenPort = 3001
LocationSendPort = 5060
Proxy_IP = "127.0.0.1"
Location_IP = "127.0.0.1"


class ProxyThread(threading.Thread):
    def __init__(self, ip, port, proxySock):
        threading.Thread.__init__(self)
        self.ip = ip
        self.port = port
        self.proxySock = proxySock
        print "New thread started for proxy"

    def run(self):
        print "Connection from: " + ip

        while True:

class locationThread(threading.Thread):
    def __init__(self, ip, port, locateSock):
        threading.Thread.__init__(self)
        self.ip = ip
        self.port = port
        self.locateSock = locateSock
        print "New thread started for location"

    def run(self):
        print "Connection from: " + ip

        while True:
    

#Create listen for proxy socket, connect and process thread
proxySock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
proxySock.bind((Proxy_IP,ProxyListenPort))
proxySock.listen(1)

(pSock, (Proxy_IP, ProxyListenPort)) = proxySock.accept()

pThread = ProxyThread(Proxy_IP, ProxyListenPort, pSock)
pThread.start()

#Create location socket, connect and process thread
while True:
    pass    
