import socket
import threading
import SocketServer


class User:
    def __init__(self, sipId, ip):
        self.sipId = sipId
        self.ip = ip
    def getSipId(self):
        return self.sipId
    def getIp (self):
        return self.ip
    def update(self, ip):
        self.ip = ip
def Singleton(cls):
    return cls()


@Singleton
class location:

    users={}
    def save(self, sipId, ip):
        self.users[sipId]  = User(sipId, ip)
        print ('ok')
        return "ok"
    def fetch(self, sipId):
        return self.users[sipId].getIp()
        


def parsePacket(data):
    type, sipId, ip = data.split()
    #arr = data.split('\r\n')
    
    #type = arr[0].split()[0]
    #sipId = arr[7].split()[1].split(":")[1].split("@")[0]
    #ip =arr[7].split()[1].split("@")[1].split(":")[0]
    print (type)
    print (sipId)
    print (ip)
    rtn = ""
    loc = location
   
    if ( type == 'REGISTER' ):
        print ("registering")
        rtn = loc.save( sipId, ip)
    if (type == 'LOOKUP'):
        print ("lookingup")
        rtn = loc.fetch(  sipId) #returns ip address
    return rtn



class ThreadedTCPRequestHandler(SocketServer.BaseRequestHandler):

    def handle(self):
        data = self.request.recv(1024)
        
        response = parsePacket( data )

        #cur_thread = threading.current_thread()
        #response = "{}: {}".format(cur_thread.name, data)


        self.request.send(response)
        server.shutdown()

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
    HOST, PORT = "localhost", 5061

    server = ThreadedTCPServer((HOST, PORT), ThreadedTCPRequestHandler)
    ip, port = server.server_address

    # Start a thread with the server -- that thread will then start one
    # more thread for each request
    server_thread = threading.Thread(target=server.serve_forever)
    # Exit the server thread when the main thread terminates
    server_thread.daemon = True
    server_thread.start()
    print ("Server loop running in thread:", server_thread.name)



#   client(ip, port, "register 1 1")
#    client(ip, port, "register 2 2")
#    client(ip, port, "register 3 3")
#    client(ip, port, "lookup 2 2")
#    server.shutdown()

while True:
    pass
