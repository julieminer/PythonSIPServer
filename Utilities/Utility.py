import socket

class Utility:
    """Utility Class for SIP Server.

    """
    
    def send_100_trying(self, srv, to, fr, call_id, cseq):
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
Content-Length: 0\n\n"
        print msg,

    
    def send_msg_udp(client_addr, ssock_udp, msg):
        """Send udp message to client.

        """

        ssock_udp.sendto(msg,client_addr);

        
        

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
