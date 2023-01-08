#zdalny logger
#komunikacja po REST API
#wypisywanie informacji na CLI
#na biezaco zapisywanie i modyfikowanie logow z alertami+akcjami wykonywanymi w programie
#GEN.MGMG.2, GEN.LOG.1
import flask
from flask import Flask, request
from datetime import datetime
import os

def log(data, function_name):
    file_name = function_name + '-' + datetime.now().strftime("%d-%m-%Y-%H:%M:%S")+'.txt'
    path = '/var/log/logs/'
    fp = path+file_name
    command = 'touch '+ fp
    os.system(command)
    with open(fp, 'w') as f:
        f.write(data)

app = Flask(__name__)

@app.route('/send', methods=['POST'])
def send_data():
    data = flask.request.get_json()
    print(data)
    return data

if __name__ == '__main__':
    app.run(host='localhost', port=5001, debug=False)
