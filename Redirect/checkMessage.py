#include Messages

# All If statments are placeholders until I figure out what to put in them
def check(msg):
	if(msg == 1): #Valid Request
		return Messages.MULTIPLE_CHOICES
	elif(msg == 2): #Moved
		return Messages.MOVE_PERMANENT
	elif(msg == 3): #Proxy
		return Messages.USE_PROXY
	else:
		return Messages.REJECTED

