
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
        return "200 OK"
    def fetch(self, sipId):
        return self.users[sipId].getIp()
        

def parsePacket(data):
    print (data)
    stuff= data.split()
    type = stuff[0]
    #arr = data.split('\r\n')
    
    #type = arr[0].split()[0]
    #sipId = arr[7].split()[1].split(":")[1].split("@")[0]
    #ip =arr[7].split()[1].split("@")[1].split(":")[0]
    print (type)
    
    rtn = ""
    loc = location
   
    if ( type == 'REGISTER' ):
        print ("registering")
        sipId, ip = stuff[1].split("@")
        rtn = loc.save( sipId, ip)
    if (type == 'LOOKUP'):
        print ("lookingup")
        sipId = stuff[1]
        rtn = loc.fetch(  sipId) #returns ip address
    return rtn


