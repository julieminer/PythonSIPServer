def checkRegister(msg):
    i = msg.find("REGISTER") 
    if (i >= 0 and i < 8):
        print "REGISTER"
	return True
    return False

def parseMsg(msg):
    print "Parsing Message"
    return msg

def OKMessage():
    msg = "SIP/2.0 200 OK"
    return msg

