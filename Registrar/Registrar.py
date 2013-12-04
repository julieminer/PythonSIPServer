import socket
import Messages
import threading
import SocketServer

ProxyListenPort = 5061
LocationSendPort = 5062
Proxy_IP = "127.0.0.1"
Location_IP = "127.0.0.1"

class ThreadedTCPRequestHandler(SocketServer.BaseRequestHandler):
   

    def handle(self):
        print "Connection from Proxy: " #+ self.proxy_ip
        self.location_ip = Location_IP
        self.location_port = LocationSendPort
        self.location_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)        
        recvMessage = self.request.recv(1024)
            
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
            self.request.send("OK")
            print "Send OK to proxy"
        
            
class ThreadedTCPServer(SocketServer.ThreadingMixIn, SocketServer.TCPServer):
    pass
if __name__ == '__main__':
    #Create listen for proxy socket, wait for connection and process thread
    HOST, PORT = "localhost", ProxyListenPort
    server = ThreadedTCPServer((HOST, PORT), ThreadedTCPRequestHandler)
    ip, port = server.server_address
    print ip
    # Start a thread with the server -- that thread will then start one
    # more thread for each request
    server_thread = threading.Thread(target=server.serve_forever)
    # Exit the server thread when the main thread terminates
    server_thread.daemon = True
    server_thread.start()
    print ("Server loop running in thread:", server_thread.name)


    input('press enter to exit')

