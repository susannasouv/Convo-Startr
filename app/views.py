from flask import render_template
from app import app

import random

import sqlite3
conn = sqlite3.connect('test.db')
c = conn.cursor()

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html') # more arguments fill in {{ ... }}

def response(name, relationship, why):
	responses = []
	keywords = get_keywords(why) # Python list of keywords
	for keyword in keywords:
		c.execute("SELECT response FROM " + relationship + " WHERE reason = " + keyword + " ;")
		responses.append(c.fetchone())
	if responses == []:
		return name + "...hi"
	return random.choice(responses)
