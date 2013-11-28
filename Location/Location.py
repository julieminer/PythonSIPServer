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
    print (data)
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

        self.request.send(response)
        

class ThreadedTCPServer(SocketServer.ThreadingMixIn, SocketServer.TCPServer):
    pass



if __name__ == "__main__":
    # Port 0 means to select an arbitrary unused port
    HOST, PORT = "", 5062

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



while True:
    pass
