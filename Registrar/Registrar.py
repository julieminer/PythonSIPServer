from socket import *

listenPort  = 3000
sendPort    = 5060
UDP_IP      = "127.0.0.1"

listenSocket = socket(AF_INET, SOCK_DGRAM)
listenSocket.bind((UDP_IP, listenPort))

sendSocket = socket(AF_INET, SOCK_DGRAM)

while True:
    message, callerAddr = listenSocket.recvfrom(1024)
    
