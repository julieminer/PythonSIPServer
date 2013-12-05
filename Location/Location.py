
import Network


if __name__ == "__main__":
    ip,port = Network.InitServer()
    testing = 1
    if( testing ):
        Network.client(ip, port, "REGISTER toto@142.232.237.133")
        Network.client(ip, port, "REGISTER bob@142.232.237.131")
        Network.client(ip, port, "REGISTER joe@142.232.237.131")
        Network.client(ip, port, "REGISTER jack@142.232.237.139")
        Network.client(ip, port, "REGISTER tom@142.232.237.134")
        input("Press enter to exit")
