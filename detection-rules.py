#reguły analityczne uzywane do detekcji zdarzen
#przekazywane do scannera
#OFF.DETPY.1.1 OFF.DETPY.1.2

import datetime

def example_rule(event):
    if event['method'] == 'POST' and event['status_code'] == '200': #and (datetime.datetime.fromisoformat(event['ts']).hour > 15 or datetime.datetime.fromisoformat(event['ts']).hour < 8):
        action_alert = "remote"
        description = "Alert: DN"
    else:
        action_alert = None
        description = None
    return action_alert, description
