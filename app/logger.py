#zdalny logger
#komunikacja po REST API
#wypisywanie informacji na CLI
#na biezaco zapisywanie i modyfikowanie logow z alertami+akcjami wykonywanymi w programie
#GEN.MGMG.2, GEN.LOG.1

from flask import Flask, request

app = Flask(__name__)

@app.route('/send', methods=['POST'])
def send_data():
    data = request.data.decode()
    print(data)
    return data

if __name__ == '__main__':
    app.run(host='localhost', port=5001, debug=False)
