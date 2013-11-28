def processError(msg, sock, addr):
	print "Processing Error"

def processAck(msg, sock, addr):
	print "Processing ACK"

def processRegister(msg, sock, addr):
	print "Processing REGISTER"

def processInfo(msg, sock, addr):
	print "Processing INFO"

def processInvite(msg, sock, addr):
	print "Processing INVITE"
	var.send_100_trying(msg)

def processOptions(msg, sock, addr):
	print "Processing OPTION"

def processCancel(msg, sock, addr):
	print "Processing CANCEL"

def processBye(msg, sock, addr):
	print "Processing BYE"
	