import checkMessage
#------------------------------
# CLIENT MESSAGE
#------------------------------
#SIP/2.0 200 OK
#Via: SIP/2.0/TCP client.atlanta.example.com:5060;branch=z9hG4bK74bf9;received=192.0.2.101
#From: Alice <sip:alice@atlanta.example.com>;tag=9fxced76sl
#To: Bob <sip:bob@biloxi.example.com>;tag=8321234356
#Call-ID: 3848276298220188511@atlanta.example.com
#CSeq: 1 INVITE
#Contact: <sip:bob@client.biloxi.example.com;transport=tcp>
#Content-Type: application/sdp
#Content-Length: 147


# Reply with this whenever a bad call is received
def REJECTED(): #404
	msg  = "SIP/2.0 404 REJECTED"
	return msg

# Reply with this when there is one or more servers to redirect to
# The Contact fields of the message should contain a list of these servers
def MULTIPLE_CHOICES(): #300
	msg = "SIP/2.0 300 MULTIPLE CHOICES\n"
	try:
		f1 = open("redirect_list", 'r')
		line = f1.read(1024)
		while line != "":
			msg += "Content: " + line
			line = f1.read(1024)
		f1.close()
	except:
		print "ERROR: File specified does not exist"
	return msg

# This tells the user that the address it is using is no longer valid and that it should update it locally
# The contact field should contain the updated address of the thingy, should one exist
def MOVE_PERMANENT(): #301
	msg = "SIP/2.0 301 MOVED PERMANENTLY"
	return msg

# This tells the user that the address it is using is temperarily not valid
# The contact field should contain the updated address of the thingy, should one exist
# It is unlikely this will ever be called
def MOVE_TEMP(): #302
	msg = "SIP/2.0 302 MOVED TEMPERARILY"
	return msg

# This tells the user to try to contact its whatever through a specific proxy, as it is the only valid path
# The contact field should contain the address of the proxy.
def USE_PROXY(): #305
	msg = "SIP/2.0 305 USE PROXY"
	return msg

