rom __future__ import with_statement
from contextlib import closing
import sqlite3, shelve, json, math, urllib
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash, escape

DEBUG = TRUE
SECRET_KEY = 'development key'

class dateclashdb:
    def __init__(self, database):
        g.db = sqlite3.connect(database)
        self.db = g.db
        
    def execute(self, command, args = None):
        if (args):
            return self.db.execute(command, args)
        else:
            return self.db.execute(command)

    def close(self):
        self.db.close()
        
    def commit(self):
        self.db.commit()


