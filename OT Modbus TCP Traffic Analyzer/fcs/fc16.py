from scapy.packet import Raw
from .mbap import mbap_parser
from report import write 

def parse_request(payload):
 write("================= WRITE OPERATION REQUEST=================")
 mbap_parser(payload)
 write(f"fc{payload[7]}   Operation         :   Write Multiple Register Request "  )
 starting_address=int.from_bytes(payload[8:10],"big")
 quantity=int.from_bytes(payload[10:12],"big")
 byte_count=payload[12]


 write(f"Starting Address  : {starting_address}")
 write(f"Quantity          : {quantity}") 
 write(f"Byte Count        : {byte_count}")

 for i in range(quantity):
  x=13+i*2
  y=x+2
  values=int.from_bytes(payload[x:y],"big")
  write(f"Register {(starting_address)+i} : {values}")
 
def parse_response(payload): 
 write("================= WRITE OPERATION RESPONSE=================")
 mbap_parser(payload)
 write(f"fc{payload[7]}   Operation         :  Write Multiple Register Response ")
 starting_address=int.from_bytes(payload[8:10],"big")
 no_of_values_written=int.from_bytes(payload[10:12],"big")
 write(f"Starting Address  : {starting_address}")
 write(f"Register Writtens : {no_of_values_written}")
 
