import socket

listenPort = 3000
sendPort   = 5060
UDP_IP     = "127.0.0.1"

listenSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
listenSocket.bind((UDP_IP, listenPort))

sendSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
	message, addr = listenSocket.recvfrom(1024)
	sendMessage = CheckMessage.check(message)
	sendSocket.sendto(sendMessage, (UDP_IP, sendPort))

