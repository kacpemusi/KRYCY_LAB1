#komunikuje sie z glowny klientem po REST API
#moze:
#przekazac glownemu hostowi informacje o swojej konfiguracji
#przechwytywac ruch sieciowy i zapisac go do pliku .pcap
#przekazac za pomoca JSONA konfiguracje zbierania
#pobieranie i przekazywanie plikow na glownego klienta
#aplikacja centralna moze na nim wykonac polecenia systemowe
#komunikacja z alertami logami itp z glownym hostem
#całe ON.REM

from flask import Flask, request, jsonify
import subprocess

app = Flask(__name__)

@app.route('/api/execute', methods=['POST'])
def execute():
    # Get the command from the request payload
    command = request.get_json()['command']

    # Execute the command and get the output
    output = subprocess.run(command, shell=True, stdout=subprocess.PIPE).stdout.decode('utf-8')

    # Return the output as a response
    return jsonify({'output': output})

if __name__ == '__main__':
    app.run(host='192.168.56.103', port=5000)
