
#wczytywanie plikow w formacie .txt/xml/json/pcap/evtx
#za pomoca re lub grepa przefiltrowanie informacji
#OFF.LOG.1, OFF.LOG.2

import os
import sys
import re
import tempfile
import subprocess
import logger
from info_generator import info_send

def search_file(file_path, regex):
	"""Search a file for a regular expression"""
	pattern = re.compile(regex)
	answer = ''
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
					answer += line
					#print(line, end='')

        # Delete the temporary XML file
		os.unlink(temp_xml_file.name)
	else:
        # If it's not an EVTX file, search the file directly
		with open(file_path, 'r') as f:
			for line in f:
				if pattern.search(line):
					#print(line, end='')
					answer += line
	return answer

# Check if the number of arguments is correct
if len(sys.argv) != 4:
	print("Usage: python files_analyzer.py PATH re/grep REGEX")
	sys.exit(1)

# Get the path and the regular expression from the command line arguments
path = sys.argv[1]
fd = 0
if os.path.isfile(path):
	fd = 1
else:
	if os.path.isdir(path):
		fd = 2
	else:
		print("Use the correct path")
		sys.exit(1)
regex = sys.argv[3]
type = sys.argv[2]
t = 0
if type == 're':
	t = 1
else:
	if type == 'grep':
		t = 2
if t == 0:
	print('Use the correct option - re or grep')
	sys.exit(1)

# File types to search
file_types = ['.txt', '.xml', '.json', '.pcap', '.evtx']
answer = ''
# Check if the path is a file or a folder
if fd == 1:
    # If it's a file, search the file if it's of a specified type
	if os.path.splitext(path)[1] in file_types:
		if t == 1:
			answer = search_file(path, regex)
		else:
			cmd = 'cat ' + path + ' | grep ' + regex
			answer = subprocess.check_output(cmd,shell=True).decode('utf-8') 
else:
    # If it's a folder, search all the files in the folder
	for root, dirs, files in os.walk(path):
		for file in files:
			if os.path.splitext(file)[1] in file_types:
				file_path = os.path.join(root, file)
				if t == 1:
					answer += search_file(file_path, regex)
				else:
					cmd = 'cat ' + file_path + ' | grep ' + regex
					answer += subprocess.check_output(cmd, shell=True).decode('utf-8')
print(answer)
logger.log(answer, 'files_analyzer')
info_send(answer)
