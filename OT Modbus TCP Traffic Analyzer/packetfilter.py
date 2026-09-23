from scapy.layers.inet import TCP,IP
from scapy.packet import Raw
from report import write
from request_parser import request_parser
from response_parser import response_parser
from statistics import packet_cal

def rawcheck(packet,packetnum):

   if packet.haslayer(Raw):
      payload=packet[Raw].load

      if packet[TCP].dport==502:
       request_parser(payload,packet,packetnum)

      if packet[TCP].sport==502:
       response_parser(payload,packet,packetnum)
   else : 
      write("Packet Don't Have Payload")

def portcheck(packet,packetnum):

 if packet[TCP].dport==502 or packet[TCP].sport==502:
    rawcheck(packet,packetnum)
    


def packetcheck(packet,packetnum):
 packet_cal()

 if packet.haslayer(TCP):
   write("====================")
   write(f" Packet {packetnum} ")
   write("====================")
   portcheck(packet,packetnum)
   
