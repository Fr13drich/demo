#!/bin/python
"""simple webpage"""
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    """return text"""
    return "Hello, my name is Fred"
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
