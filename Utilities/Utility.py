from socket import *
import re

class Utility:
    """Utility Class for SIP Server.

    """
    
    def get_100_trying(self, srv, to, fr, call_id, cseq):
        """Send 100 Trying.

        This message is sent when the server receives an INVITE
        """
        
        msg = "\
SIP/2.0 100 Trying\n\
Via: SIP/2.0/UDP "+srv+";received=192.0.2.1\n\
To: "+to+"\n\
From: "+fr+"\n\
Call-ID: "+call_id+"\n\
CSeq: "+cseq+"\n\
Content-Length: 0"
        return msg

    def parse_invite(self, msg):
        """Generate 100 OK message from an INVITE message.

        """
        
        #get INVITE first line
        eol_1 = msg.find("\r\n")
        #print msg[:eol_1]

        #tokenize headers
        parsed = re.findall(r"(?P<name>.*?): (?P<value>.*?)\r\n", msg)

        #print parsed

        srv = ""
        to = ""
        fr = ""
        call_id = ""
        cseq = ""

        for p in parsed:
            if(p[0] == "Via"):
                srv = p[1][p[1].find(" ")+1:]
            if(p[0] == "To"):
                to = p[1]
            if(p[0] == "From"):
                fr = p[1]
            if(p[0] == "Call-ID"):
                call_id = p[1]
            if(p[0] == "CSeq"):
                cseq = p[1]
            #print p[0],p[1]

        return self.get_100_trying(srv, to, fr, call_id, cseq)
    
    def send_ok_msg(self, client_addr, ssock_udp, msg):
        """Send 100 OK message to client.

        """
        send_msg = self.parse_invite(msg)
        ssock_udp.sendto(send_msg,client_addr)
        #print "Sent message to:",client_addr," Contents:"
        #print send_msg

    def parse_register(self,msg):
        """Generate 100 OK message from an INVITE message.

        """
        """
        msg = "REGISTER sip:142.232.253.225 SIP/2.0\n\
Via: SIP/2.0/UDP 142.232.253.220:5060;rport;branch=z9hG4bK30813\n\
From: <sip:jeremy@142.232.253.225>;tag=5003\n\
To: <sip:jeremy@142.232.253.225>\n\
Call-ID: 6448\n\
CSeq: 6 REGISTER\n\
Contact: <sip:jeremy@142.232.253.220;line=3d3c2d5799b9597>\n\
Max-Forwards: 70\n\
User-Agent: Linphone/3.6.1 (eXosip2/3.6.0)\n\
Expires: 3600\n\
Content-Length: 0"
        """
        
        #Extract REGISTER line
        eol_1 = msg.find("\n")
        msg1 = msg[:eol_1+1]
        msg2 = msg.replace(msg1,"")

        #Extract Max-Forwards line
        eol_2 = msg.find("Max-Forwards:")
        eol_3 = msg.find("User-Agent")
        msg3 = msg[eol_2:eol_3]
        msg4 = msg2.replace(msg3,"")

        #Add 200 OK to beginning
        msg5 = "SIP/2.0 200 OK\n" + msg4
        return msg5



"""
#Test parse_register
U = Utility()
U.parse_register()
"""
#Test send ok message function
'''
#create socket to listen for INVITE
ssock = socket(AF_INET, SOCK_DGRAM)
ssock.bind(('localhost',5060))

#listen for message
#print "Listening"
msg, addr = ssock.recvfrom(2048)


#print addr
#Test parse method
U = Utility()
#print U.parse_invite(msg)
U.send_ok_msg(addr,ssock,msg)

#close socket
ssock.close()
'''


#Test parsing
"""
#create socket to listen for INVITE
ssock = socket(AF_INET, SOCK_DGRAM)
ssock.bind(('localhost',5063))

#listen for message
print "Listening"
msg, addr = ssock.recvfrom(2048)

#get INVITE first line
eol_1 = msg.find("\r\n")
#print msg[:eol_1]

#tokenize headers
parsed = re.findall(r"(?P<name>.*?): (?P<value>.*?)\r\n", msg)

print parsed

srv = ""
to = ""
fr = ""
call_id = ""
cseq = ""

for p in parsed:
    if(p[0] == "Via"):
        srv = p[1][p[1].find(" ")+1:]
    if(p[0] == "To"):
        to = p[1]
    if(p[0] == "From"):
        fr = p[1]
    if(p[0] == "Call-ID"):
        call_id = p[1]
    if(p[0] == "CSeq"):
        cseq = p[1]
    print p[0],p[1]
    

    

#close socket
ssock.close()

#Test send_100_trying using invite fields
U = Utility()
U.send_100_trying(srv, to, fr, call_id, cseq)
"""




#Test send_100_trying
"""        
U = Utility()
test_var = ('pc33.atlanta.com;branch=z9hG4bKnashds8'
                ,'Bob <sip:bob@biloxi.com>'
                ,'Alice <sip:alice@atlanta.com>;tag=1928301774'
                ,'a84b4c76e66710'
                ,'314159 INVITE')
U.send_100_trying(*test_var)
"""
