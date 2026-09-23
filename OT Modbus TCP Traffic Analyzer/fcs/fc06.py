from scapy.packet import Raw
from .mbap import mbap_parser
from scapy.layers.inet import TCP,IP
from report import write

def parse_request(payload):
  
  write("================= WRITE OPERATION REQUEST=================")
  mbap_parser(payload)
  write(f"fc{payload[7]}   Operation     :  Write Single Register Request ")
  register_address=int.from_bytes(payload[8:10],"big")
  value=int.from_bytes(payload[10:12],"big")
  write(f"Register Address : {register_address}")
  write(f"Value to Write   : {value}")

def parse_response(payload):
  
  write("================= WRITE OPERATION RESPONSE=================")
  mbap_parser(payload)
  write(f"fc{payload[7]}   Operation     :   Write Single Register Response ")
  reg_address=int.from_bytes(payload[8:10],"big")
  value=int.from_bytes(payload[10:12],"big")
  write(f"The Value {value}is written on the Register {reg_address}")

