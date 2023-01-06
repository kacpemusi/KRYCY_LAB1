#aplikacja glowna agenta w trybie CLI
#obsluguje po prostu uzytkownika
#GEN.MGMT.6 i 6.1, GEN.AGT.1 ,

import requests
import sys

if len(sys.argv) != 2:
    print("Usage: agent_command.py COMMAND")

# Set the API endpoint URL
url = 'http://192.168.56.1:5000/api/execute'

# Set the command to be executed
command = sys.argv[1]

# Send the request with the command as the payload
response = requests.post(url, json={'command': command})

# Get the output from the response
output = response.json()['output']

# Print the output
print(output)
