#otwieranie plikow .pcap
#filtrowanie z formatem BPF
#wyswietlanie pakietów
#OFF.PCAP.1, OFF.PCAP.2

import sys
import pyshark
# Check if the number of arguments is correct
if len(sys.argv) != 3:
    print("Usage: python pcap_analyzer.py PCAP_FILE BPF_FILTER")
    sys.exit(1)

# Get the PCAP file and BPF filter from the command line arguments
pcap_file = sys.argv[1]
bpf_filter = sys.argv[2]

# Open the PCAP file
pcap = pyshark.FileCapture(pcap_file, display_filter=bpf_filter)
for packet in pcap:
    print(packet)
