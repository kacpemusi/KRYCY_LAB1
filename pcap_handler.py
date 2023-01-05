#otwieranie plikow .pcap
#filtrowanie z formatem BPF
#wyswietlanie pakietów
#OFF.PCAP.1, OFF.PCAP.2

import pcapy
import sys
import struct
import socket
# Check if the number of arguments is correct
if len(sys.argv) != 3:
    print("Usage: python pcap_analyzer.py PCAP_FILE BPF_FILTER")
    sys.exit(1)

# Get the PCAP file and BPF filter from the command line arguments
pcap_file = sys.argv[1]
bpf_filter = sys.argv[2]

# Open the PCAP file
pcap = pcapy.open_offline(pcap_file)

# Set the BPF filter
pcap.setfilter(bpf_filter)

# Process the packets
header, data = pcap.next()
while header is not None:
    ip_header = data[:20]
    ip_header_unpacked = struct.unpack('!BBHHHBBH4s4s', ip_header)
    ip_version = ip_header_unpacked[0] >> 4
    ip_header_length = ip_header_unpacked[0] & 0x0F
    ip_ttl = ip_header_unpacked[5]
    ip_protocol = ip_header_unpacked[6]
    ip_source = socket.inet_ntoa(ip_header_unpacked[8])
    ip_destination = socket.inet_ntoa(ip_header_unpacked[9])

    # Print the packet information
    print(f'Timestamp: {header.getts()}')
    print(f'Length (bytes): {header.getlen()}')
    print(f'Source IP: {ip_source}')
    print(f'Destination IP: {ip_destination}')
    print(f'Protocol: {ip_protocol}')
    # Get the next packet
    header, data = pcap.next()

# Close the PCAP file
pcap.close()

