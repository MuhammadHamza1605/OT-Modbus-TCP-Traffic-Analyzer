from report import write

stats = {
    "total_packets": 0,
    "requests": 0,
    "responses": 0,
    "read_operations": 0,
    "write_operations": 0,
    "exceptions": 0,
    "malformed": 0,

    "fc01": 0,
    "fc02": 0,
    "fc03": 0,
    "fc04": 0,
    "fc05": 0,
    "fc06": 0,
    "fc15": 0,
    "fc16": 0,
    "write_single_coil":0,
    "write_single_register":0,
    "write_multiple_coils":0,
    "write_multiple_registers":0
}

def packet_cal():
    stats["total_packets"] += 1
def request_cal():
    stats["requests"] += 1
def response_cal():
    stats["responses"] += 1
def exception_cal():
    stats["exceptions"] += 1
def malformed():
    stats["malformed"] += 1

def write_operation_cal():
    write("")
    write("="*70)
    write("WRITE OPERATION STATISTICS")
    write("="*70)
    write(f"Write Single Coil          : {stats['write_single_coil']}")
    write(f"Write Single Register      : {stats['write_single_register']}")
    write(f"Write Multiple Coils       : {stats['write_multiple_coils']}")
    write(f"Write Multiple Registers   : {stats['write_multiple_registers']}")
    write("="*70)

def functioncode(fc):

    if fc == 1:
        stats["fc01"] += 1
        stats["read_operations"] += 1

    elif fc == 2:
        stats["fc02"] += 1
        stats["read_operations"] += 1

    elif fc == 3:
        stats["fc03"] += 1
        stats["read_operations"] += 1

    elif fc == 4:
        stats["fc04"] += 1
        stats["read_operations"] += 1

    elif fc == 5:
        stats["fc05"] += 1
        stats["read_operations"] += 1
        stats["write_single_coil"] += 1

    elif fc == 6:
        stats["fc06"] += 1
        stats["write_operations"] += 1
        stats["write_single_register"] += 1

    elif fc == 15:
        stats["fc15"] += 1
        stats["write_operations"] += 1
        stats["write_multiple_coils"] += 1

    elif fc == 16:
        stats["fc16"] += 1
        stats["write_operations"] += 1
        stats["write_multiple_registers"] += 1

def summary():
    write("")
    write("="*70)
    write("SUMMARY")
    write("="*70)
    write(f"Total Packets          : {stats['total_packets']}")
    write(f"Requests               : {stats['requests']}")
    write(f"Responses              : {stats['responses']}")
    write("")
    write(f"Read Operations        : {stats['read_operations']}")
    write(f"Write Operations       : {stats['write_operations']}")
    write("")
    write(f"Exception Responses    : {stats['exceptions']}")
    write(f"Malformed Packets      : {stats['malformed']}")
    write("")
    write("="*70)
    write("FUNCTION CODE STATISTICS")
    write("="*70)
    write(f"FC01 Read Coils                : {stats['fc01']}")
    write(f"FC02 Read Discrete Inputs      : {stats['fc02']}")
    write(f"FC03 Read Holding Registers    : {stats['fc03']}")
    write(f"FC04 Read Input Registers      : {stats['fc04']}")
    write(f"FC05 Write Single Coil         : {stats['fc05']}")
    write(f"FC06 Write Single Register     : {stats['fc06']}")
    write(f"FC15 Write Multiple Coils      : {stats['fc15']}")
    write(f"FC16 Write Multiple Registers  : {stats['fc16']}")
    write("="*70)
    write_operation_cal()
