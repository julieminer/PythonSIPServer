import socket
import Messages
import threading

ProxyListenPort = 5061
LocationSendPort = 5060
Proxy_IP = "127.0.0.1"
Location_IP = "127.0.0.1"
regMsg = ''

class ProxyThread(threading.Thread):
    def __init__(self, ip, port, proxySock):
        threading.Thread.__init__(self)
        self.ip = ip
        self.port = port
        self.proxySock = proxySock
        print "New thread started for Proxy"

    def run(self):
        print "Connection from Proxy: " + self.ip
                
        while True:
            recvMessage = self.proxySock.recv(1024)
            
            if(Messages.checkRegister(recvMessage) == True):
                regMsg = Messages.parseMsg(recvMessage)
                print regMsg
            else:
                continue
                
class LocationThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.ip = Location_IP
        self.port = LocationSendPort
        self.locateSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print "New thread started for location"

    def run(self):
        print "Connection to Location: " + self.ip
        self.locateSock.connect((self.ip, self.port))

        while True:
            if len(regMsg) == 0:
                continue
            else:
                self.locateSock.send(regMsg)
                self.locateSock.recv(1024)
                                

if __name__ == '__main__':
    #Create listen for proxy socket, wait for connection and process thread
    proxySock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    proxySock.bind((Proxy_IP,ProxyListenPort))
    proxySock.listen(1)

    (pSock, (Proxy_IP, ProxyListenPort)) = proxySock.accept()

    proxyThread = ProxyThread(Proxy_IP, ProxyListenPort, pSock)
    locationThread = LocationThread()
    
    proxyThread.start()
    locationThread.start()

    proxyThread.join()
    locationThread.join()
