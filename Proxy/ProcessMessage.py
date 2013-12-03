def processError(msg, addr, utils, socks):
	print "Processing Error"
	# ignore errors

def processAck(msg, addr, utils, socks):
	print "Processing ACK"

def processRegister(msg, addr, utils, socks):
	print "Processing REGISTER"
	socks[0].send(msg)

def processInfo(msg, addr, utils, socks):
	print "Processing INFO"

def processInvite(msg, addr, utils, socks):
	print "Processing INVITE"
	sendTrying(msg, addr, utils, socks)
	userAddress = lookupUser(msg, socks)
	if(userAddress != "NO USER"):
		sendInvite(msg, userAddress, socks)

def processOptions(msg, addr, utils, socks):
	print "Processing OPTION"
	# don't do this
	
def processCancel(msg, addr, utils, socks):
	print "Processing CANCEL"
	# this sucks, ignore it

def processBye(msg, addr, utils, socks):
	print "Processing BYE"
	# send bye to whoever
	
def sendTrying(msg, addr, utils, socks):
	utils.send_ok_msg(addr, socks[3], msg)

def sendInvite(msg, userAddress, socks):
	print "Send Invite to ", userAddress
	clientAddress = ((userAddress, 3001))
	socks[3].sendto(msg, clientAddress)

def lookupUser(msg, socks):
	name = getToName(msg)
	socks[2].send("LOOKUP " + name)
	address = socks[2].recv(1024)
	address = "192.168.0.1"
	if(address == ""):
		return "NO USER"
	return address

def processRinging(msg, addr, utils, socks):
	print "Ringing"

def getFromName(msg):
	nameStart 	= msg.find(";tag")
	nameEnd 	= msg.find("From: ")
	return msg[nameEnd:nameStart]

def getToName(msg):
	nameStart 	= msg.find("From: ")
	nameEnd 	= msg.find("To: ")
	name  		= msg[nameEnd:nameStart]
	return name