import socket
import CheckMessage

def start(utils, socks):
	print "server start"
	listenPort 		= 5060
	sendPort		= 5060
	UDP_IP 			= "192.168.0.2"
	listenSocket 	= socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	clientSocket 	= socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	clientAddress 	= (UDP_IP, sendPort)
	listenSocket.bind((UDP_IP, listenPort))
	socks.append(listenSocket)

	while True:
		message, addr = listenSocket.recvfrom(1024)
		CheckMessage.options[CheckMessage.check(message)](message, addr, utils, socks)

