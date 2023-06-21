#!/bin/python

from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello, my name is Fred"
app.run(host="0.0.0.0", port=80)

