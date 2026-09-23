from scapy.layers.inet import IP
from report import write
from statistics import malformed

SUPPORTED_FUNCTION_CODES = {
    1, 2, 3, 4,
    5, 6,
    15, 16
}

def validation_error(packet, packetnum, reason):
    malformed()
    write("")
    write("="*70)
    write(f"WARNING : MALFORMED MODBUS PACKET {packetnum}")
    write("="*70)
    write(f"Source IP        : {packet[IP].src}")
    write(f"Destination IP   : {packet[IP].dst}")
    write("")
    write(f"Reason           : {reason}")
    write("Packet Skipped")
    write("="*70)
    write("")


def validate(payload, packet, packetnum):

    if len(payload) < 8:
        validation_error(packet, packetnum, "Payload length is less than MBAP Header.")
        return False

    protocol = int.from_bytes(payload[2:4], "big")
    if protocol != 0:
        validation_error(packet, packetnum,f"Invalid Protocol ID ({protocol})")
        return False

    length = int.from_bytes(payload[4:6], "big")
    if length != len(payload[6:]):
        validation_error(packet, packetnum,"Length Field does not match actual payload.")
        return False

    fc = payload[7]
    if fc >= 0x80:
        fc -= 0x80
    if fc not in SUPPORTED_FUNCTION_CODES:
        validation_error(packet, packetnum, f"Unsupported Function Code ({fc})")
        return False

    return True
