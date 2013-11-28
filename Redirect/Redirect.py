import socket
import Messages
import checkMessage

listenSocket = socket.socket() #TCP is the default
host = ''    #Refers to local Machine
port = 3000

listenSocket.bind((host, port))

listenSocket.listen(5)
while True:
	client, address = listenSocket.accept()

	message, addr = listenSocket.recvfrom(1024)
	sendMessage = CheckMessage.check(message)
	client.send(sendMessage)

