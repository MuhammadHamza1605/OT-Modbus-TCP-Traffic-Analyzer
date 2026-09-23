from scapy.packet import Raw
from scapy.layers.inet import TCP,IP
from .mbap import mbap_parser
from report import write

def parse_request(payload):
  mbap_parser(payload)
  write(f"fc{payload[7]}   Operation     :   Read Input Register Request ")
  starting_address=int.from_bytes(payload[8:10],"big")
  quantity=int.from_bytes(payload[10:12],"big")
  write(f"Starting Address : {starting_address}")
  write(f"Quantity         : {quantity}")

def parse_response(payload):
  mbap_parser(payload)
  write(f"fc{payload[7]}   Operation     :  Read Input Register Response")
  write(f"Byte Counts      : {payload[8]}")
  total_reg=(payload[8])//2
  write(f"Total Registers  : {total_reg}")

  for  i in range(total_reg):
   x=9+i*2
   y=x+2
   values=int.from_bytes(payload[x:y],"big")
   write(f"Register {i} :  {values} ")
