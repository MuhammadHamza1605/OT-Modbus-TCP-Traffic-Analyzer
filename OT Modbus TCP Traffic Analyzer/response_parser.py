from scapy.all import Raw
from scapy.layers.inet import IP
from dispatcher import response
from statistics import response_cal,exception_cal
from report import write
from validator import validate
from tracker import track_response

exception_codes = {
    1: "Illegal Function",
    2: "Illegal Data Address",
    3: "Illegal Data Value",
    4: "Slave Device Failure",
    5: "Acknowledge",
    6: "Slave Device Busy",
    8: "Memory Parity Error",
    10: "Gateway Path Unavailable",
    11: "Gateway Target Device Failed to Respond"
}

def exception_parser(payload, packet):

    function_code = payload[7]
    original_fc = function_code - 0x80
    exception_code = payload[8]

    write(f"Source IP        : {packet[IP].src}")
    write(f"Destination IP   : {packet[IP].dst}")
    write("")
    write("************ EXCEPTION RESPONSE ************")
    write(f"Function Code    : FC{original_fc:02d}")
    write(f"Exception Code   : {exception_code}")
    write(f"Description      : {exception_codes.get(exception_code,'Unknown Exception')}")
    write("********************************************")

def response_parser(payload, packet,packetnum):

    if not validate(payload,packet,packetnum):
      return
    functioncode = payload[7]
    if functioncode >= 0x80:
        exception_cal()
        exception_parser(payload, packet)
    parser = response.get(functioncode)
    if parser:
        response_cal()
        write(f"Source IP        : {packet[IP].src}")
        write(f"Destination IP   : {packet[IP].dst}")
        parser(payload)
        track_response(payload,packet)
    else:
        write(f"Unknown Function Code : {functioncode}")
