#!/usr/bin/env python3.10
import flask
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    formatted_response = format_response({'answer': 'data'})
    return formatted_response


@app.route('/pilot')
def pilot():
    formatted_response = format_response({'answer': 'piloting'})
    return formatted_response


# DO NOT CHANGE
def format_response(json: any):
    response = flask.jsonify(json)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


# DO NOT CHANGE
if __name__ == '__main__':
    app.run()
