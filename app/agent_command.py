#aplikacja glowna agenta w trybie CLI
#obsluguje po prostu uzytkownika
#GEN.MGMT.6 i 6.1, GEN.AGT.1 ,

import requests
import sys
from datetime import datetime

if len(sys.argv) < 2:
    print("Usage: agent_command.py COMMAND(pcap, download, execute, list, ifconfig)")
    sys.exit(1)
# Set the API endpoint URL
url = 'http://10.0.2.15:5000/api/execute'

# Set the command to be executed
match sys.argv[1]:
    case 'pcap':
        path = '/var/log/pcap_agent/'+datetime.now().strftime("%d-%m-%Y-%H:%M:%S")+'.pcap'
        command = 'tshark -w '+path+' -i '+sys.argv[2]+' -a duration:'+sys.argv[3]+'; sleep 0.5; sshpass -p PASSWORD scp '+path+' omegalul@10.0.2.15:/home/omegalul/Desktop/pcaps/'
    case 'download':
        command = 'sshpass -p PASSWORD scp /var/log/logs_agent/'+sys.argv[2]+' omegalul@10.0.2.15:/home/omegalul/Desktop/logs/'
    case 'execute':
        command = sys.argv[2]
    case 'list':
        command = 'ls /var/log/logs_agent/'
    case 'ifconfig':
        command = 'ifconfig'
    case other:
        print("Usage: agent_command.py COMMAND(pcap, download, execute, list, ifconfig)")
        sys.exit(1)
# Send the request with the command as the payload
response = requests.post(url, json={'command': command})

# Get the output from the response
output = response.json()['output']

# Print the output
print(output)
