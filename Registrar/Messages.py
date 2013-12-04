def checkRegister(msg):
    i = msg.find("REGISTER") 
    if (i >= 0 and i < 8):
        print "REGISTER"
        return True
    return False

def parseMsg(msg):
    firstIndex = msg.find("To: <sip:")
    lastIndex = msg.find(">", firstIndex)
    sipAddr = msg[firstIndex + 9:lastIndex]
    return "REGISTER " + sipAddr

def OKMessage():
    msg = "SIP/2.0 200 OK"
    return msg

