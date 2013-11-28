import socket
from Proxy import Proxy 
from Utilities import Utility
import Registrar

regAddress = "localhost"
redAddress = "localhost" 
locAddress = "localhost"

RegistrarSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
RegistrarSocket.bind((regAddress, 5061))
RedirectSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
RedirectSocket.bind((redAddress, 5062))
LocationSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
LocationSocket.bind((locAddress, 5063))

U = Utility.Utility()
Proxy.start(U)
