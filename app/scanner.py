#skaner zagrozen
#korzysta z sigma rules LYB py rules
#nastepnie je laduje i skanuje wybrane pliki z wymaganymi rozszerzeniami
#GEN.MGMT.3,4
#GEN.MGMT.5.1
#OFF.DETPY.2
#REG.DET.2
#from sigma_handler import *
import os
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
        event_data = {"ts": a_data[0], "uid": a_data[1], "id.orig_h": a_data[2], "id_orig_p": a_data[3], "id.resp_h": a_data[4], "id.resp_p": a_data[5], "trans_depth": a_data[6], "method": a_data[7], "host": a_data[8], "uri": a_data[9], "referrer": a_data[10], "user_agent": a_data[11], "request_body_len": a_data[12], "response_body_len": a_data[13], "status_code": a_data[14], "status_msg": a_data[15], "info_code": a_data[16], "info_msg": a_data[17], "filename": a_data[18], "tags": a_data[19], "username": a_data[20], "password": a_data[21], "proxied": a_data[22], "orig_fuids": a_data[23], "orig_mime_types": a_data[24], "resp_fuids": a_data[25], "resp_mime_types": a_data[26]} 
    else:
        event_data = None
    return event_data

example_events = extract_events('../log.txt')
for event in example_events:
    print(detection_rules.example_rule(event))

os.system('cd ../Zircolite; python3 zircolite.py --events LM_NewShare_Added_Sysmon_12_13.evtx --rules rules/rules_linux.json')
