import socket
from Proxy import Proxy 
from Utilities import Utility
from Registrar import Registrar

regAddress = "localhost"
redAddress = "localhost" 
locAddress = "localhost"

RegistrarSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
RegistrarSocket.connect((regAddress, 5061))
RedirectSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#RedirectSocket.connect((redAddress, 5062))
LocationSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
LocationSocket.connect((locAddress, 5062))

socks = [RegistrarSocket, RedirectSocket, LocationSocket]

U = Utility.Utility()
Proxy.start(U, socks)
