#!/usr/bin/python3

"""
********************************************************************************
** Authors:
** Data Visualizer - Evin Colignon (colignoe@oregonstate.edu)
** Crawler Developer - James Hippler (hipplerj@oregonstate.edu)
** Data Transfer Developer - Victor Wang (wangv@oregonstate.edu)
**
** Oregon State University
** CS 467-400 (Summer 2018)
** Online Capstone Project
**
** Project Group Lyra: Graphical Crawler (WEB2)
** Description: Python Crawler Application for Breadth-First/Depth-First URL
** web searches.
** Due: Friday, August 17, 2018
**
** Filename: main.py
**
** External Resources:
** - https://www.youtube.com/watch?v=zRwy8gtgJ1A
********************************************************************************
"""

import sys
sys.path.append('web_crawler/')                                                 # Add the python crawler directory to the system path
import threading
from flask import Flask, render_template, url_for, redirect, request, make_response
from wtforms import Form, StringField, IntegerField, RadioField, validators
import crawler as crawl


app = Flask(__name__)

class SearchForm(Form):
    starting_url    = StringField('Starting URL', [validators.Length(min=1), validators.URL(message='Please Enter a Valid URL (example https://oregonstate.edu)'), validators.InputRequired()])
    method          = RadioField('Search Method', choices=[('breadth','Breadth First'),('depth','Depth First')], validators = [validators.InputRequired(message='A Search Method must be Selected')])
    depth           = IntegerField('Search Depth', [validators.InputRequired(message='Search Depth Maximum is 3 for Breadth and 100 for Depth')])
    keyword         = StringField('Keyword (Optional)')

# Routing for the Home (main) page
@app.route('/')
def index():
    return render_template('home.html')

# Routing for the Search Form Page
@app.route('/search', methods=['GET', 'POST'])
def search():
    form = SearchForm(request.form)
    # if request.method == 'POST' and form.validate():
    if request.method == 'POST':
        # crawler_thread = threading.Thread(target=crawl.crawler, args=form.data)
        # crawler_thread.start()
        # app.logger.info(form.data)
        # crawl.crawler(form.data)      # Call function to perform crawl using the Form submissions on the the search routes

        response = make_response(redirect(url_for('results', code=307)))
        response.set_cookie('urls', form.starting_url.data)



        return response
    return render_template('search.html', form=form)

# Routing for Search Results
@app.route('/results', methods=['GET', 'POST'])
def results():
    return render_template('results.html')

if __name__ == '__main__':
    app.run(debug=True, port=7777, threaded=True)
