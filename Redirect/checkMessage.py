#include Messages

# All If statments are placeholders until I figure out what to put in them
def check(msg):
	if(msg == 300): #Valid Request
		return Messages.MULTIPLE_CHOICES
	elif(msg == 301): #Moved
		return Messages.MOVE_PERMANENT
	elif(msg == 305): #Proxy
		return Messages.USE_PROXY
	else:
		return Messages.REJECTED

