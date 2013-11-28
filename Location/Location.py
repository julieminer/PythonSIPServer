import socket
import threading
import SocketServer


class User:
    def __init__(self, sipId, ip):
        self.sipId = sipId
        self.ip = ip
    def getSipId():
        return self.sipId
    def getIp ():
        return self.ip
    def update( ip):
        self.ip = ip
def Singleton(cls):
    return cls()


@Singleton
class location:
        
    def __init__(self):
        print 'Foo created'
    users={}
    def save(self, sipId, ip):
        self.users[sipId]  = User(sipId, ip)
        return "ok"
    def fetch(self, sipId):
        self.users[sipId].getIp()
        return "ok"


def parsePacket(data):
    type, sipId, ip = data.split()
    print (type)
    print (sipId)
    print (ip)
    rtn = ""
    loc = location
    print loc
    if ( type == 'register' ):
        rtn = loc.save( sipId, ip)
    if (type == 'lookup'):
        rtn = loc.fetch(  sipId) #returns ip address
    return rtn



class ThreadedTCPRequestHandler(SocketServer.BaseRequestHandler):

    def handle(self):
        data = self.request.recv(1024)
        
        response = parsePacket( data )

        #cur_thread = threading.current_thread()
        #response = "{}: {}".format(cur_thread.name, data)


        self.request.sendall(response)

class ThreadedTCPServer(SocketServer.ThreadingMixIn, SocketServer.TCPServer):
    pass

def client(ip, port, message):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((ip, port))
    try:
        sock.sendall(message)
        response = sock.recv(1024)
        print ("Received: {}".format(response))
    finally:
        sock.close()

if __name__ == "__main__":
    # Port 0 means to select an arbitrary unused port
    HOST, PORT = "localhost", 9050

    server = ThreadedTCPServer((HOST, PORT), ThreadedTCPRequestHandler)
    ip, port = server.server_address

    # Start a thread with the server -- that thread will then start one
    # more thread for each request
    server_thread = threading.Thread(target=server.serve_forever)
    # Exit the server thread when the main thread terminates
    server_thread.daemon = True
    server_thread.start()
    print ("Server loop running in thread:", server_thread.name)

    client(ip, port, "register 1 1")
    client(ip, port, "register 2 2")
    client(ip, port, "register 3 3")

    server.shutdown()


