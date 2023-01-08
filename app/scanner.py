#skaner zagrozen
#korzysta z sigma rules LYB py rules
#nastepnie je laduje i skanuje wybrane pliki z wymaganymi rozszerzeniami
#GEN.MGMT.3,4
#GEN.MGMT.5.1
#OFF.DETPY.2
#REG.DET.2
#from sigma_handler import *
import os
import sys
import logger
from info_generator import *
detection_rules = __import__('detection-rules')

def extract_events(log_file):
    events = []
    # Read the log file line by line
    with open(log_file, 'r') as f:
        for line in f:
            # Use a regular expression to extract the event data from the line
            event_data = extract_event_data(line)
            if event_data:
                events.append(event_data)
    return events

def extract_event_data(line):
    a_data = line.split("\t")
    if (len(a_data)==27):
        event_data = {"ts": a_data[0], "uid": a_data[1], "id.orig_h": a_data[2], "id.orig_p": a_data[3], "id.resp_h": a_data[4], "id.resp_p": a_data[5], "trans_depth": a_data[6], "method": a_data[7], "host": a_data[8], "uri": a_data[9], "referrer": a_data[10], "user_agent": a_data[11], "request_body_len": a_data[12], "response_body_len": a_data[13], "status_code": a_data[14], "status_msg": a_data[15], "info_code": a_data[16], "info_msg": a_data[17], "filename": a_data[18], "tags": a_data[19], "username": a_data[20], "password": a_data[21], "proxied": a_data[22], "orig_fuids": a_data[23], "orig_mime_types": a_data[24], "resp_fuids": a_data[25], "resp_mime_types": a_data[26]} 
    elif (len(a_data)==23):
        event_data = {"ts": a_data[0], "uid": a_data[1], "id.orig_h": a_data[2], "id.orig_p": a_data[3], "id.resp_h": a_data[4], "id.resp_p": a_data[5], "proto": a_data[6], "trans_id": a_data[7], "query": a_data[8], "qclass": a_data[9], "qclass_name": a_data[10], "qtype": a_data[11], "qtype_name": a_data[12], "rcode": a_data[13], "rcode_name": a_data[14], "AA": a_data[15], "TC": a_data[16], "RD": a_data[17], "RA": a_data[18], "Z": a_data[19], "answers": a_data[20], "TTLs": a_data[21], "rejected": a_data[22]}
    else:
        event_data = None
    return event_data

#if (len(sys.argv)!=4):
    #print("Usage: python3 scanner.py python PATH RULE_OPTION(http, dns or all)")
    #print("Usage: python3 scanner.py sigma PATH_TO_EVENTS PATH_TO_RULES")
    #sys.exit(1)

#if ((len(sys.argv) != 4) and (sys.argv[1] == "python")):
    #print("Usage: python3 scanner.py python PATH RULE_OPTION(http, dns or all)") 
    #sys.exit(1)

#elif (len(sys.argv) != 4 and sys.argv[1] == "sigma"):
    #print("Usage: python3 scanner.py sigma PATH_TO_EVENTS PATH_TO_RULES")
    #sys.exit(1)
answer = ''
flag = False
match sys.argv[1]:
    case "python":
        example_events = extract_events(sys.argv[2])
        for event in example_events:
            match sys.argv[3]:
                case "http":
                    if detection_rules.rule_http(event) != (' '):
                        #print(detection_rules.rule_http(event))
                        answer += '------------------------------------------------------\n' + 'Scanning using python rule http\n' + '------------------------------------------------------\n' + detection_rules.rule_http(event) + '\n'
			print(answer)
			info_send(detection_rules.rule_http(event))
                #case "dns":
                #    if detection_rules.rule_dns(event) != (' '):
                #        print(detection_rules.rule_dns(event))
		#	answer += 
                #        info_send(detection_rules.rule_dns(event))
                case "all":
                    if detection_rules.rule_http(event) != (' '):
                        #print(detection_rules.rule_http(event))
                        answer += '------------------------------------------------------\n' + 'Scanning using python rule http\n' + '------------------------------------------------------\n' + detection_rules.rule_http(event) + '\n'
			#info_send(detection_rules.rule_http(event))
                        flag = True
                case "blip":
                    answer += '------------------------------------------------------\n' + 'Scanning using python rule blip\n' + '------------------------------------------------------\n' + detection_rules.rule_blacklist(pcap=['/home/omegalul/Desktop/dupa.pcapng'],txt=['dns.txt']) + '\n'
                    print(answer)
                case other:
                    print("Usage: python3 scanner.py python PATH RULE_OPTION(http, dns or all)")
                    sys.exit(1)

    case "sigma":
	cmd = 'cd ../Zircolite; python3 zircolite.py --events '+sys.argv[2]+' --rules '+sys.argv[3]
        answer = subprocess.check_output(cmd,shell=True).decode('utf-8')
	print(answer)
    case other:
        print("Options: python or sigma")
if flag:
    answer += '------------------------------------------------------\n' + 'Scanning using python rule blip\n' + '------------------------------------------------------\n' + detection_rules.rule_blacklist(pcap=['/home/omegalul/Desktop/dupa.pcapng'],txt=['dns.txt']) + '\n'
    print(answer)
logger.log(answer,'scanner')
