#informacje o alertach/logach/wykonanych akcjach itp sa tu przetwarzane aby nastepnie zostaly wyslane do
#zdalnego loggera po rest API
#poza loggerem alerty rowniez do glownego klienta CLI przekazywane do wyswietlenia

import requests

def info_send(data):
    url = 'http://localhost:5001/send'
    headers = {'Content-Type': 'text/plain'}
    response = requests.post(url, data=data, headers=headers)
