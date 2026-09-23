from scapy.packet import Raw
from .mbap import mbap_parser
from report import write
value={
 0xFF00:"ON",
 0x0000:"OFF"}

def parse_request(payload):
 
 write("================= WRITE OPERATION REQUEST=================")
 mbap_parser(payload)
 write(f"fc{payload[7]}   Operation    :   Write Single Coil Request ")
 address=int.from_bytes(payload[8:10],"big")
 write(f"Address         : {address}")
 coilvalue=int.from_bytes(payload[10:12],"big")
 setvalue=value.get(coilvalue,"Unknown Value")
 write(f"Set Value       : {setvalue}")
def parse_response(payload):
 
 write("================= WRITE OPERATION RESPONSE=================")
 mbap_parser(payload)
 write(f"fc{payload[7]}   Operation    :   Write Single Coil Response " )
 coilvalue=int.from_bytes(payload[10:12],"big")
 setvalue=value.get(coilvalue,"Unknown Value")
 address=int.from_bytes(payload[8:10],"big")
 write(f"The value is set as : {setvalue}  at the Address : {address}")
