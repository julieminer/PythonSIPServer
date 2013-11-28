from socket import *
import Messages

listenPort      = 3001
sendPort        = 5060
UDP_IP          = "127.0.0.1"

listenSocket = socket(AF_INET, SOCK_DGRAM)
listenSocket.bind(('', listenPort))

sendSocket = socket(AF_INET, SOCK_DGRAM)

while True:
    message, callerAddr = listenSocket.recvfrom(1024)

    # Check to see if message is a REGISTER message
    if(Messages.checkRegister(message) == True):
        recvMessage = Messages.parseMsg(message)
        print recvMessage
    else:
        continue
  
    # If the REGISTER message is valid, send Client Information
    # to Location Server and send an OK message to client.
    
    sendSocket.sendto(recvMessage, (UDP_IP, sendPort))
    print Messages.OKMessage
    
