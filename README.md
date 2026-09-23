# OT Network Traffic Analyzer – Modbus TCP Protocol Analyzer

An offline **OT Network Traffic Analyzer** for analyzing **Modbus TCP network traffic from PCAP files**. The project parses captured packets, identifies Modbus operations, validates request/response communication, tracks transactions, handles exceptions, collects statistics, and generates a structured text report.

## Project Overview

Modbus TCP is widely used in industrial environments but does not provide built-in encryption, authentication, or integrity protection. This project provides an offline tool for analyzing captured Modbus TCP traffic and extracting useful protocol-level information for OT cybersecurity analysis.

The analyzer:

- Reads Modbus TCP traffic from `.pcap` files
- Filters relevant TCP traffic using port `502`
- Extracts Modbus TCP/MBAP information
- Identifies supported Modbus function codes
- Parses Modbus requests and responses
- Matches requests and responses using Transaction ID
- Detects missing responses
- Handles Modbus exception responses
- Collects read/write operation statistics
- Generates a text-based analysis report

> **Scope:** This project performs offline PCAP analysis. It does not actively communicate with PLCs or other industrial devices.

## Architecture

```text
                    ┌──────────────────────┐
                    │     PCAP Input       │
                    │       .pcap          │
                    └──────────┬───────────┘
                               ↓
                    ┌──────────────────────┐
                    │ Packet Capture Reader│
                    │       Scapy          │
                    └──────────┬───────────┘
                               ↓
                    ┌──────────────────────┐
                    │    Packet Filter     │
                    │   TCP / Port 502     │
                    └──────────┬───────────┘
                               ↓
                    ┌──────────────────────┐
                    │ Validation & Payload │
                    │      Extraction      │
                    └──────────┬───────────┘
                               ↓
                    ┌──────────────────────┐
                    │    MBAP / PDU Parser │
                    └──────────┬───────────┘
                               ↓
                    ┌──────────────────────┐
                    │ Function-Code        │
                    │     Dispatcher       │
                    └──────────┬───────────┘
                               ↓
          ┌────────────────────┴────────────────────┐
          ↓                                         ↓
┌─────────────────────────┐             ┌─────────────────────────┐
│   Modbus FC Parsers     │             │ Exception / Response   │
│ FC01 FC02 FC03 FC04     │             │       Validation        │
│ FC05 FC06 FC15 FC16     │             └────────────┬────────────┘
└────────────┬────────────┘                          ↓
             └────────────────┬─────────────────────┘
                              ↓
                  ┌────────────────────────┐
                  │ Transaction ID Tracking│
                  │ / Missing Responses    │
                  └────────────┬───────────┘
                               ↓
                  ┌────────────────────────┐
                  │ Statistics & Report    │
                  │       Generation       │
                  └────────────┬───────────┘
                               ↓
                  ┌────────────────────────┐
                  │   Final Text Report    │
                  │ <pcap_name>_report.txt │
                  └────────────────────────┘
```

## Features

### Supported Modbus Function Codes

| Function Code | Operation |
|---|---|
| `01` | Read Coils |
| `02` | Read Discrete Inputs |
| `03` | Read Holding Registers |
| `04` | Read Input Registers |
| `05` | Write Single Coil |
| `06` | Write Single Register |
| `15 / 0F` | Write Multiple Coils |
| `16 / 10` | Write Multiple Registers |

### Traffic Analysis

The analyzer extracts information including:

- Source IP address
- Destination IP address
- Modbus Transaction ID
- Modbus function code
- Starting address
- Quantity of registers/coils
- Register values
- Coil values
- Byte count
- Request/response information
- Exception information

### Transaction Tracking

Requests and responses are tracked using the **Modbus Transaction Identifier**.

The analyzer can identify:

- Matching request/response pairs
- Responses associated with requests
- Requests for which no response was observed

### Statistics

The report includes statistics such as:

- Total packets analyzed
- Read operations
- Write operations
- Single-write operations
- Multiple-write operations
- Coil/register write breakdown

## Technologies Used

- **Python**
- **Scapy**
- **Modbus TCP**
- **Wireshark** for packet inspection and validation
- **PCAP** files for offline traffic analysis

## Project Structure

```text
OT-Network-Traffic-Analyzer/
│
├── main.py
├── packetfilter.py
├── validator.py
├── tracker.py
├── report.py
├── statistics.py
├── dispatcher.py
│
├── fcs/
│   ├── fc_01.py
│   ├── fc_02.py
│   ├── fc_03.py
│   ├── fc_04.py
│   ├── fc_05.py
│   ├── fc_06.py
│   ├── fc_15.py
│   ├── fc_16.py
│   └── ...
│
├── pcapfiles/
│   └── *.pcap
│
├── reports/
│   └── *_report.txt
│
└── README.md
```

> The exact file structure may vary depending on the final project version.

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/MuhammadHamza1605/OT-Modbus-TCP-Traffic-Analyzer
cd OT-Network-Traffic-Analyzer
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the virtual environment

**Linux / Kali Linux:**

```bash
source venv/bin/activate
```

**Windows:**

```powershell
venv\Scripts\activate
```

### 4. Install Scapy

```bash
pip install scapy
```

## Usage

Place a Modbus TCP PCAP file inside the `pcapfiles` directory or provide its path directly.

Run:

```bash
python main.py <pcap_file>
```

Example:

```bash
python main.py pcapfiles/Modbus_TCP_INT16.pcap
```

The analyzer generates a report in the `reports` directory.

Example:

```text
reports/Modbus_TCP_INT16_report.txt
```

## Example Report

A generated report contains information similar to:

```text
======================================================================
           MODBUS TCP TRAFFIC ANALYSIS REPORT
======================================================================

Input File     : Modbus_TCP_INT16.pcap
Generated On   : ...

Source IP      : 192.168.x.x
Destination IP : 192.168.x.x

Function Code  : 03
Operation      : Read Holding Registers
Starting Address : ...
Quantity         : ...

Transaction ID : ...

----------------------------------------------------------------------
Statistics
----------------------------------------------------------------------

Total Packets       : ...
Read Operations     : ...
Write Operations    : ...
Single Writes       : ...
Multiple Writes     : ...

======================================================================
END OF REPORT
======================================================================
```

## Testing

The analyzer was tested using Modbus TCP PCAP files containing different operations, including:

- Read operations
- Single write operations
- Multiple write operations
- Coil operations
- Register operations
- Request/response communication
- Exception responses
- Missing response scenarios

Wireshark can be used to inspect the original PCAP traffic and compare it with the analyzer output.

## Security Relevance

Modbus TCP does not inherently provide mechanisms such as:

- Encryption
- Authentication
- Message integrity protection

Therefore, visibility into Modbus TCP traffic can support OT security monitoring and protocol analysis.

This project focuses specifically on **offline protocol analysis**, providing a practical way to inspect Modbus TCP communication and identify protocol-level events from captured network traffic.

## Limitations

- The analyzer operates on **offline PCAP files**.
- It does not perform live network monitoring.
- Asset inventory is outside the current project scope.
- Analysis depends on the availability and quality of captured traffic.
- Traffic that does not use the expected Modbus TCP port may not be identified by the current filtering approach.

## Future Enhancements

Possible future improvements include:

- Live Modbus TCP traffic monitoring
- Web-based dashboard
- Graphical traffic visualization
- Automated anomaly detection
- Support for additional Modbus function codes
- Asset/device identification
- CSV/JSON report generation
- SIEM or OT monitoring integration
- Alert generation for suspicious Modbus operations

## Project Information

**Project:** OT Network Traffic Analyzer – Modbus TCP Protocol Analyzer  
**Student:** Muhammad Hamza  
**Program:** BSc Computer and Information Sciences  
**Institution:** Pakistan Institute of Engineering & Applied Sciences (PIEAS)  
**Industry Supervisor:** Qasim Ali  
**Year:** 2026

## License

This project was developed as an academic/internship project. Add an appropriate open-source license if the repository is intended for public redistribution.

## Author

**Muhammad Hamza**

Computer Science / Computer & Information Sciences Student  
Interested in **OT/ICS Cybersecurity, Network Security, and Industrial Protocol Analysis**.
