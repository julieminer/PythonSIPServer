import ProcessMessage
p = ProcessMessage

options = { -1 : p.processError,
			 0 : p.processAck,
			 1 : p.processRegister,
			 2 : p.processInfo,
			 3 : p.processInvite,
			 4 : p.processOptions,
			 5 : p.processCancel,
			 6 : p.processBye}

def checkInvite(msg):
	i = msg.find("INVITE") 
	if (i >= 0 & i < 6):
		return True
	return False

def checkAck(msg):
	i = msg.find("ACK") 
	if (i >= 0 and i < 3):
		print "ACK"
		return True
	return False

def checkBye(msg):
	i = msg.find("BYE") 
	if (i >= 0 and i < 3):
		print "BYE"
		return True
	return False

def checkCancel(msg):
	i = msg.find("CANCEL") 
	if (i >= 0 and i < 5):
		print "CANCEL"
		return True
	return False

def checkOptions(msg):
	i = msg.find("OPTIONS") 
	if (i >= 0 and i < 7):
		print "OPTIONS"
		return True
	return False

def checkRegister(msg):
	i = msg.find("REGISTER") 
	if (i >= 0 and i < 8):
		print "REGISTER"
		return True
	return False

def checkInfo(msg):
	i = msg.find("INFO") 
	if (i >= 0 and i < 4):
		print "INFO"
		return True
	return False

def check(msg):
	if checkAck(msg):
		return 0
	elif (checkRegister(msg)):
		return 1
	elif (checkInfo(msg)):
		return 2
	elif (checkInvite(msg)):
		return 3
	elif (checkOptions(msg)):
		return 4
	elif (checkCancel(msg)):
		return 5
	elif (checkBye(msg)):
		return 6
	else:
		return -1