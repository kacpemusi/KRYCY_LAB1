#otwieranie plikow .pcap
#filtrowanie z formatem BPF
#wyswietlanie pakietów
#OFF.PCAP.1, OFF.PCAP.2

import sys
import os
import pyshark
import logger
from info_generator import info_send
# Check if the number of arguments is correct
if len(sys.argv) != 3 and len(sys.argv) != 2:
    print("Usage: python pcap_analyzer.py PCAP_FILE [BPF_FILTER]")
    sys.exit(1)
packets = ''
# Get the PCAP file and BPF filter from the command line arguments
pcap_file = sys.argv[1]
if not os.path.isfile(pcap_file):
    print('Pass the correct path to file')
if len(sys.argv) == 3:
    bpf_filter = sys.argv[2]
    pcap = pyshark.FileCapture(pcap_file, display_filter=bpf_filter)
    for packet in pcap:
        packets += str(packet)
else:
    pcap = pyshark.FileCapture(pcap_file)
    for packet in pcap:
        packets += str(packet)
print(packets)
logger.log(packets, 'pcap_handler')
info_send(packets.encode('utf-8'))
