from scapy.all import Raw
from scapy.layers.inet import IP
from dispatcher import request
from statistics import request_cal,functioncode
from report import write
from validator import validate

from tracker import track_request
def  request_parser(payload,packet,packetnum):
  
  if not validate(payload,packet,packetnum):
     return
  track_request(payload,packet)
  fc=payload[7]
  functioncode(fc)
  parser=request.get(fc,"Unknown FunctionCode")
  
  if parser:
    request_cal()
    write(f"Source IP        : {packet[IP].src}")
    write(f"Destination IP   : {packet[IP].dst}")
    parser(payload)
  else:
    write(f"NO Function Found for the FunctionCode  : {parser} {paypload[7]}")
