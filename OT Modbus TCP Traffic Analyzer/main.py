import sys
import os
from tracker import report_missing,transaction_summary
from report import set_report,write
from scapy.all import rdpcap
import packetfilter
from statistics import summary
from datetime import datetime

def header():
  write("="*70)
  write("           MODBUS TCP TRAFFIC ANALYSIS REPORT")
  write("="*70)
  write(f"Input File     : {filename}")
  write(f"Generated On   : {datetime.now().strftime('%d-%m-%Y %H:%M:%S')}")
  write("="*70)
  write("")

def footer():
 write("")
 write("="*70)
 write("END OF REPORT") 
 write("="*70)

if len(sys.argv)!=2:
  print("Usage:")
  print("python3 main.py <pcapfile>")
  sys.exit()

pcap_file=sys.argv[1]

if not os.path.isfile(pcap_file):
   print("Error : File not Found ")
   sys.exit()

packets= rdpcap(pcap_file)
filename=os.path.basename(pcap_file)
name=os.path.splitext(filename)[0]
report_file=open(f"reports/{name}_report.txt","w")
set_report(report_file)
header()

for packetnum,packet in enumerate(packets,start=1):
  packetfilter.packetcheck(packet,packetnum)

write(f"Total Packets are : {len(packets)}")
report_missing()
transaction_summary()
summary()
footer()
report_file.close()
print("=" * 60)
print("Analysis Completed Successfully")
print(f"Input File   : {filename}")
print(f"Packets      : {len(packets)}")
print(f"Report Saved : reports/{name}_report.txt")
print("=" * 60)
