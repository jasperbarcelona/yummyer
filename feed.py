import flask, flask.views
from flask import render_template
from flask import session, redirect
from jinja2 import environment, FileSystemLoader
from flask import url_for, request, session, redirect
import time
import os


app = flask.Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index_route():
    return flask.render_template('index.html')

if __name__ == '__main__':
    app.debug = True
    app.run()