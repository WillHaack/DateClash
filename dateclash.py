#!/usr/bin/python                                                             
from __future__ import with_statement
from contextlib import closing
import sqlite3, shelve
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash, escape

DATABASE = '/tmp/dateclash.db'
DEBUG = True
SECRET_KEY = 'development key'
PORT = 5050
db = None
app = Flask(__name__)

app.config.from_object(__name__)
app.config.from_envvar('FLASKR_SETTINGS', silent=True)

def init_db():
    with closing(sqlite3.connect('/tmp/dateclash.db')) as db1:
        with app.open_resource('schema.sql') as f:
            db1.cursor().executescript(f.read())
        db1.commit()

@app.before_request
def before_request():
    pass
#TODO : connect to db

@app.teardown_request
def teardown_request(exception):
    pass
#TODO : close connection to db

@app.route('/')
def index():
    return render_template('index.html')

#@app.route('/register', method="POST")
#def register():
#    return render_template('register.html')

if __name__ == '__main__':
    app.run("localhost", port=PORT)
