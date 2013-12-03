def processError(msg, utils, socks):
	print "Processing Error"
	# ignore errors

def processAck(msg, utils, socks):
	print "Processing ACK"

def processRegister(msg, utils, socks):
	print "Processing REGISTER"
	#forwardToRegistrar(msg)
	socks[0].send(msg)

def processInfo(msg, utils, socks):
	print "Processing INFO"

def processInvite(msg, utils, socks):
	print "Processing INVITE"
	#socks[0].send(msg)
	sendTrying(msg)
	user = lookupUser(msg, socks)
	if(user != "NO USER"):
		sendInvite(user)

def processOptions(msg, utils, socks):
	print "Processing OPTION"
	# don't do this
	
def processCancel(msg, utils, socks):
	print "Processing CANCEL"
	# this sucks, ignore it

def processBye(msg, utils, socks):
	print "Processing BYE"
	
	# send bye to whoever
	
def sendTrying(msg):
	print "send trying"
	#get the address from the msg
	#send TRYING message to address

def sendInvite(user):
	print "Send Invite"
	#send invite to users address

def lookupUser(msg, socks):
	name = getName(msg)
	#socks[2].send("LOOKUP " + name)
	#address = socks[2].recv(1024)
	address = "192.168.0.1"
	if(address == ""):
		return "NO USER"
	return address

def getName(msg):
	print "getting name"
	nameStart 	= msg.find(";tag")
	nameEnd 	= msg.find("From: ")
	nameSize	= nameEnd - nameStart
	print "namestart = ", nameStart
	print "nameEnd = ", nameEnd 
	name  		= msg[nameEnd:nameStart]
	print name
	return name