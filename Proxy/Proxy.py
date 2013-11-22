import socket
import CheckMessage

listenPort 		= 5060
UDP_IP 			= "127.0.0.1"
listenSocket 	= socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
listenSocket.bind((UDP_IP, listenPort))

while True:
	message, addr = listenSocket.recvfrom(1024)
	CheckMessage.options[CheckMessage.check(message)](message)

