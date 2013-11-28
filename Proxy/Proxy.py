import socket
import CheckMessage

listenPort 		= 5060
sendPort		= 3001
UDP_IP 			= "192.168.56.1"
listenSocket 	= socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
clientSocket 	= socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
clientAddress 	= ((UDP_IP, sendPort))
listenSocket.bind((UDP_IP, listenPort))

while True:
	message, addr = listenSocket.recvfrom(1024)
	CheckMessage.options[CheckMessage.check(message)](message, clientSocket, clientAddress)

