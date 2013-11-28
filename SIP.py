import socket
from Proxy import Proxy 
from Utilities import Utility
import Registrar

regAddress = "142.232.237.141"
redAddress = "localhost" 
locAddress = "localhost"

RegistrarSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
RegistrarSocket.connect((regAddress, 5061))
RedirectSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#RedirectSocket.connect((redAddress, 5062))
LocationSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#LocationSocket.connect((locAddress, 5063))

socks = [RegistrarSocket, RedirectSocket, LocationSocket]

U = Utility.Utility()
Proxy.start(U, socks)
