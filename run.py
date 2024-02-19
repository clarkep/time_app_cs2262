from flask import Flask
app = Flask(__name__)

import time
import os

@app.route('/')
def hello_world():
    return 'Hello world!'

@app.route('/time')
def show_time():
    os.environ["TZ"] = "US/Eastern"
    time.tzset()
    lt = time.localtime()
    s1 = time.strftime("It's %I:%M %p.", lt)
    return s1

app.run(host='0.0.0.0',
        port=8080,
        debug=True)
