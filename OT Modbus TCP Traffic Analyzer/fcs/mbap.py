from report import write
from scapy.packet import Raw


def mbap_parser(payload):
  transaction_id=int.from_bytes(payload[0:2],"big")
  protocol=int.from_bytes(payload[2:4],"big")
  length=int.from_bytes(payload[4:6],"big")
  unit_id=payload[6]
  write(f"Transaction ID   : {transaction_id}")
  write(f"Protocol         : {protocol}")
  write(f"Length           : {length}")
  write(f"Unit ID          : {unit_id}")  
