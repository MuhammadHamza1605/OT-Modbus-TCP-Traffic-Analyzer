from scapy.packet import Raw
from report import write
from .mbap import mbap_parser
status={ 0:"OFF",1:"ON"}

def parse_request(payload):
 mbap_parser(payload)
 write(f"fc{payload[7]}  Operation   : Read Coils Request ")
 starting_address=int.from_bytes(payload[8:10],"big")
 quantity=int.from_bytes(payload[10:12],"big")
 write(f"Starting Address        : {starting_address}")
 write(f"Quantity                : {quantity}")

def parse_response(payload): 
 mbap_parser(payload)
 write(f"fc{payload[7]}  Operation   : Read Coils Response ")
 write(f"Byte Count       : {payload[8]}")
 bytecount=payload[8]
 x=1

 for i in range(bytecount):
  currentbyte=payload[9+i]
  write(f">>> Current Byte {i} <<<")

  for i in range(8):
   bit =(currentbyte>>i) & 1
   st=status.get(bit,"Invalid Status")
   write(f"Coil {x}  : {st}")
   x+=1
