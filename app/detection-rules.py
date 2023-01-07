#reguły analityczne uzywane do detekcji zdarzen
#przekazywane do scannera
#OFF.DETPY.1.1 OFF.DETPY.1.2

import datetime
import pyshark as ps
import re
import nest_asyncio

def rule_http(event):
    if ('method' in event.keys()) and ('status_code' in event.keys()):
        if event['method'] == 'POST' and event['status_code'] == '200': #and (datetime.datetime.fromisoformat(event['ts']).hour > 15 or datetime.datetime.fromisoformat(event['ts']).hour < 8):
            action_alert = "remote"
            description = event['ts']+" Alert: TEST RULE FOR OK POST"
        else:
            action_alert = ''
            description = ''
        return action_alert+" "+description
    else:
        return ' '

def rule_dns(event):
    if 'id.resp_h' in event.keys():
        if event['id.resp_h'] == '194.165.17.4':
            action_alert = "local"
            description = event['ts']+" Alert: TEST RULE FOR SUS IP"
        else:
            action_alert = ''
            description = ''
        return action_alert+" "+description
    else:
        return ' '

def rule_blacklist(**kwargs):
    nest_asyncio.apply()
    bl_ip = ['74.125.224.77', '74.125.224.89', '74.125.224.90','66.22.243.25']
    action_alert = ''
    description = ''

    for pcap_file in kwargs['pcap']:
        traffic = ps.FileCapture(pcap_file)
        ips2 = []
        for packet in traffic:
            if 'IP' in packet:
                for ip in [packet['IP'].dst, packet['IP'].src]:
                    if ip in bl_ip and ip not in ips2: 
                        description += (f'Alert: {ip} found in {pcap_file}\n')
                        ips2.append(ip)
    for file in kwargs['txt']:
        f = open(file, mode='r')
        c = f.read()
        ips = re.findall(r'\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b', c)
        for ip in ips:
            if ip in bl_ip:
                description += (f'Alert: {ip} found in {file}\n')
                action_alert='remote'
    return action_alert+' '+description

