#wczytywanie plikow w formacie .txt/xml/json/pcap/evtx
#za pomoca re lub grepa przefiltrowanie informacji
#OFF.LOG.1, OFF.LOG.2

import os
import sys
import re
import tempfile

def search_file(file_path, regex):
    """Search a file for a regular expression"""
    pattern = re.compile(regex)

    # If the file is an EVTX file, convert it to XML first
    if os.path.splitext(file_path)[1] == '.evtx':
        # Create a temporary XML file
        temp_xml_file = tempfile.NamedTemporaryFile(delete=False, suffix='.xml')
        temp_xml_file.close()

        # Convert the EVTX file to XML
        os.system(f'wevtutil epl {file_path} {temp_xml_file.name}')

        # Search the XML file
        with open(temp_xml_file.name, 'r') as f:
            for line in f:
                if pattern.search(line):
                    print(line, end='')

        # Delete the temporary XML file
        os.unlink(temp_xml_file.name)
    else:
        # If it's not an EVTX file, search the file directly
        with open(file_path, 'r') as f:
            for line in f:
                if pattern.search(line):
                    print(line, end='')

# Check if the number of arguments is correct
if len(sys.argv) != 3:
    print("Usage: python files_analyzer.py PATH REGEX")
    sys.exit(1)

# Get the path and the regular expression from the command line arguments
path = sys.argv[1]
regex = sys.argv[2]

# File types to search
file_types = ['.txt', '.xml', '.json', '.pcap', '.evtx']

# Check if the path is a file or a folder
if os.path.isfile(path):
    # If it's a file, search the file if it's of a specified type
    if os.path.splitext(path)[1] in file_types:
        search_file(path, regex)
else:
    # If it's a folder, search all the files in the folder
    for root, dirs, files in os.walk(path):
        for file in files:
            if os.path.splitext(file)[1] in file_types:
                file_path = os.path.join(root, file)
                search_file(file_path, regex)
