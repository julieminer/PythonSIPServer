
import Network


if __name__ == "__main__":
    ip,port = Network.InitServer()
    testing = 1
    if( testing ):
        Network.client(ip, port, "REGISTER toto@192.168.0.3")
        Network.client(ip, port, "REGISTER bob@192.168.0.9")
        Network.client(ip, port, "REGISTER World2@2.2.3.4")
        Network.client(ip, port, "REGISTER World@1.2.3.4")
        Network.client(ip, port, "LOOKUP World")
        input("Press enter to exit")
