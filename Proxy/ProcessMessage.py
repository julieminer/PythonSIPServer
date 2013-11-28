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
	
	