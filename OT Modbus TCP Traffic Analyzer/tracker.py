from scapy.layers.inet import IP
from report import write

function_names = {
    1: "Read Coils",
    2: "Read Discrete Inputs",
    3: "Read Holding Registers",
    4: "Read Input Registers",
    5: "Write Single Coil",
    6: "Write Single Register",
    15: "Write Multiple Coils",
    16: "Write Multiple Registers"
}

transactions = {}

matched = 0
missing = 0
unexpected = 0


def track_request(payload, packet):

    transactionid = int.from_bytes(payload[0:2], "big")
    functioncode = payload[7]

    transactions[transactionid] = {
        "operation": function_names.get(functioncode, "Unknown"),
        "source": packet[IP].src,
        "destination": packet[IP].dst
    }


def track_response(payload, packet):

    global matched
    global unexpected

    transactionid = int.from_bytes(payload[0:2], "big")

    if transactionid in transactions:

        matched += 1
        del transactions[transactionid]

    else:

        unexpected += 1

        write("")
        write("=" * 70)
        write("UNEXPECTED RESPONSE")
        write("=" * 70)
        write(f"Transaction ID : {transactionid}")
        write(f"Source IP      : {packet[IP].src}")
        write(f"Destination IP : {packet[IP].dst}")
        write("Reason         : No Matching Request Found")
        write("=" * 70)


def report_missing():

    global missing

    if len(transactions) == 0:
        return

    write("")
    write("=" * 70)
    write("MISSING RESPONSES")
    write("=" * 70)

    for transactionid, data in transactions.items():

        missing += 1

        write(f"Transaction ID : {transactionid}")
        write(f"Operation      : {data['operation']}")
        write(f"Source IP      : {data['source']}")
        write(f"Destination IP : {data['destination']}")
        write("Status         : Response Not Found")
        write("-" * 70)


def transaction_summary():

    write("")
    write("=" * 70)
    write("TRANSACTION SUMMARY")
    write("=" * 70)
    write(f"Matched Transactions      : {matched}")
    write(f"Missing Responses         : {missing}")
    write(f"Unexpected Responses      : {unexpected}")
    write("=" * 70)
