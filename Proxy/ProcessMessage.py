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
	socks[0].send(msg)
	sendTrying(msg)
	if((user = lookupUser(msg)) != "NO USER"):
		sendInvite(user)
	# send trying to client
	# LOOKUP username
	# send to address

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
	#get the address from the msg
	#send TRYING message to address

def sendInvite(user):
	#send invite to users address

def lookupUser(msg):
	#send message to location server
	name = getName(msg)
	socks[2].send("LOOKUP " + name)
	address = socks[2].recv(1024)
	#wait for response to come back
	#if no user exists, return NO USER
	if(address == ""):
		return "NO USER"
	return address

def getName(msg):
	nameStart 	= msg.find("To: ")
	nameEnd 	= msg.find("From: ")
	nameSize	= nameEnd - nameStart
	return msg.read(nameSize, nameStart)