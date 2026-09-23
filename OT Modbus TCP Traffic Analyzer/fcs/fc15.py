from scapy.packet import Raw
from report import write
from .mbap import mbap_parser

status={ 0:"OFF",1:"ON"}

def parse_request(payload):
 write("================= WRITE OPERATION REQUEST=================")
 mbap_parser(payload)
 write(f"fc{payload[7]}  Operation   : Write Multiple  Coils Request ")
 starting_address=int.from_bytes(payload[8:10],"big")
 quantity=int.from_bytes(payload[10:12],"big")
 byte_count=payload[12]
 write(f"Starting Address        : {starting_address}")
 write(f"Quantity                : {quantity}")
 write(f"Byte Count              : {byte_count}")
 x=0

 for i in range(byte_count):
   current_byte=payload[13+i]
   write(f"Current Byte {current_byte}")

   for i in range(8):
    bit=(current_byte>>i) & 1 
    st=status.get(bit,"Invalid Status")
    write(f"Bit {bit} > Coil {starting_address+x} : {st}")
    x+=1 

def parse_response(payload):
 write("================= WRITE OPERATION RESPONSE=================")
 mbap_parser(payload)
 write(f"fc{payload[7]}  Operation   : Write Multiple  Coils Response ")
 starting_address=int.from_bytes(payload[8:10],"big")
 write(f"Starting Address : {starting_address}")
 quantity_written=int.from_bytes(payload[10:12],"big")
 write(f"Number of Coils are written : {quantity_written}")
