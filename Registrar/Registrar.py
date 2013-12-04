import socket
import Messages
import threading

ProxyListenPort = 5061
LocationSendPort = 5062
Proxy_IP = "127.0.0.1"
Location_IP = "127.0.0.1"

class ProxyThread(threading.Thread):
    def __init__(self, proxy_ip, proxy_port, proxySock):
        threading.Thread.__init__(self)
        self.location_ip = Location_IP
        self.location_port = LocationSendPort
        self.location_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.proxy_ip = proxy_ip
        self.proxy_port = proxy_port
        self.proxy_sock = proxySock
        print "New thread started for Proxy"

    def run(self):
        print "Connection from Proxy: " + self.proxy_ip
                
        recvMessage = self.proxy_sock.recv(1024)
            
        if(Messages.checkRegister(recvMessage) == True):
            regMsg = Messages.parseMsg(recvMessage)
            print regMsg
            
            self.location_sock.connect((self.location_ip, self.location_port))
            print "Connect with location"            
            self.location_sock.send(regMsg)
            print "Sending location register id"

            response = self.location_sock.recv(1024)
            print "Recv from location: " + response

            self.location_sock.close()
            print "Close Connection with location"
            self.proxy_sock.send("OK")
            print "Send OK to proxy"

if __name__ == '__main__':
    #Create listen for proxy socket, wait for connection and process thread

    while True:
        #Create socket and connect to Proxy Server
        proxySock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        proxySock.bind((Proxy_IP,ProxyListenPort))
        proxySock.listen(1)
        (pSock, (Proxy_IP, ProxyListenPort)) = proxySock.accept()
        proxyThread = ProxyThread(Proxy_IP, ProxyListenPort, pSock)    
        proxyThread.start()
        proxySock.close()
        
    

