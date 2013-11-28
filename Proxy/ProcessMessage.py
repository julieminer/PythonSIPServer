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
	sendOK(sock, addr)

def processOptions(msg, sock, addr):
	print "Processing OPTION"

def processCancel(msg, sock, addr):
	print "Processing CANCEL"

def processBye(msg, sock, addr):
	print "Processing BYE"

	
def sendOK(sock, addr):
	print "sending OK"
	sock.sendto("SIP/2.0 200 OK Via: SIP/2.0/UDP server10.biloxi.com ;branch=z9hG4bKnashds8;received=192.0.2.3 Via: SIP/2.0/UDP bigbox3.site3.atlanta.com ;branch=z9hG4bK77ef4c2312983.1;received=192.0.2.2 Via: SIP/2.0/UDP pc33.atlanta.com ;branch=z9hG4bK776asdhds ;received=192.0.2.1 To: Bob <sip:bob@biloxi.com>;tag=a6c85cf From: Alice <sip:alice@atlanta.com>;tag=1928301774 Call-ID: a84b4c76e66710@pc33.atlanta.com CSeq: 314159 INVITE Contact: <sip:bob@192.0.2.4> Content-Type: application/sdp Content-Length: 131", addr)
	