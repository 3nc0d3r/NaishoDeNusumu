#!/usr/bin/env python
import socket
import sys
def listen_quietly(dest):
 try :  
  s = socket.socket(socket.AF_INET,socket.SOCK_RAW,socket.getprotobyname('icmp'))
  s.setsockopt(socket.SOL_IP, socket.IP_HDRINCL, 0)
  
  my_socket = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.getprotobyname('icmp'))
  while 1:
    data,addr = s.recvfrom(4096)
    my_socket.connect((dest, 0))
    my_socket.sendall(data)
    my_socket.close() 
    #print "Packet from %r: %r" % (addr,data)
    print data
    
    
 except KeyboardInterrupt :
    print ''
if __name__ == "__main__":
	boss = sys.argv[1]
	listen_quietly(boss)
