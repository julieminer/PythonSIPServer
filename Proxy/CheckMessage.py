import ProcessMessage
p = ProcessMessage

options = { -1 : p.processError,
			 4 : p.processAck,
			 8 : p.processRegister,
			 5 : p.processInfo,
			 0 : p.processInvite,
			 6 : p.processOptions,
			 7 : p.processCancel,
			 2 : p.processBye,
			 1 : p.processRinging,
			 3 : p.processOK}

def checkInvite(msg):
	i = msg.find("INVITE") 
	if (i == 0):
		return True
	return False
	
def checkRinging(msg):
	i = msg.find("180 Ringing")
	if (i >= 0):
		return True
	return False

def checkAck(msg):
	i = msg.find("ACK") 
	if (i == 0):
		return True
	return False

def checkBye(msg):
	i = msg.find("BYE") 
	if (i == 0):
		return True
	return False

def checkCancel(msg):
	i = msg.find("CANCEL") 
	if (i == 0):
		return True
	return False

def checkOptions(msg):
	i = msg.find("OPTIONS") 
	if (i == 0):
		return True
	return False

def checkRegister(msg):
	i = msg.find("REGISTER") 
	if (i == 0):
		return True
	return False
	
def checkOK(msg):
	i = msg.find("200 OK") 
	if (i >= 0):
		return True
	return False

def checkInfo(msg):
	i = msg.find("INFO") 
	if (i ==0):
		print "INFO"
		return True
	return False
	
def check(msg):
	i = -1
	
	if checkInvite(msg):
		return 0
	if (checkRinging(msg)):
		return 1
	if (checkBye(msg)):
		return 2
	if (checkOK(msg)):
		return 3
	if (checkAck(msg)):
		return 4
	if (checkInfo(msg)):
		return 5
	if (checkOptions(msg)):
		return 6
	if (checkCancel(msg)):
		return 7
	if (checkRegister(msg)):
		return 8
	return -1