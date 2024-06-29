import os
import time

import flask
from flask import Flask

app = Flask(__name__)

VOLUME_NAME = 'volume'
VOLUME_TEST_NAME = 'volume-test'
MODEL_FILE_NAME = 'my-model'


# https://everai.expvent.com/api/v1/apps/default/get-start/txt2img
# curl -X POST -H'Content-Type: application/json' http://localhost:8866/txt2img/jone -d '{"prompt": "say hello to"}'
@app.route('/txt2img/<name>', methods=['POST'])
def txt2img(name: str):
    data = flask.request.json
    print(data)
    prompt = data['prompt']
    time.sleep(3)
    return f"{prompt} - {name}"

# curl http://localhost:8866/show-volume
@app.route('/show-volume', methods=['GET'])
def show_volume():
    model_path = os.path.join(VOLUME_NAME, MODEL_FILE_NAME)
    with open(model_path, 'r') as f:
        return f.read()

# curl http://localhost:8866/show-volume-test
@app.route('/show-volume-test', methods=['GET'])
def show_volume_test():
    model_path = os.path.join(VOLUME_TEST_NAME, MODEL_FILE_NAME)
    with open(model_path, 'r') as f:
        return f.read()

# https://everai.expvent.com/api/routes/v1/default/get-start/sse
# http://localhost:8866/sse
@app.route('/sse', methods=['GET'])
def sse():
    def generator():
        for i in range(10):
            yield f"hello again {i}"
            time.sleep(1)

    return flask.Response(generator(), mimetype='text/event-stream')

@app.route('/healthy-check', methods=['GET'])
def healthy():
    resp = 'container is ready'
    return resp

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=False, port=8866)
