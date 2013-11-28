def processError(msg, utils):
	print "Processing Error"
	# ignore errors

def processAck(msg, utils):
	print "Processing ACK"

def processRegister(msg, utils):
	print "Processing REGISTER"
	# forwardToRegistrar(msg)

def processInfo(msg, utils):
	print "Processing INFO"

def processInvite(msg, utils):
	print "Processing INVITE"
	# send trying to client
	# LOOKUP username
	# send to address

def processOptions(msg, utils):
	print "Processing OPTION"
	# don't do this
	
def processCancel(msg, utils):
	print "Processing CANCEL"
	# this sucks, ignore it

def processBye(msg, utils):
	print "Processing BYE"
	# send bye to whoever
	
	