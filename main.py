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
@app.route('/search', methods=['POST'])
def search():

    # instantiate WTForm object
    form = SearchForm(request.form)
    print(form)

    # check for previously set cookies
    url_cookie = request.cookies.get('urls')
    delimiter = ", "   # delimiter for urls when they're saved as a string

    # If the user has posted valid data from the form
    # if request.method == 'POST' and form.validate():
    if request.method == 'POST':

        # Call crawler
        # crawler_thread = threading.Thread(target=crawl.crawler, args=form.data)
        # crawler_thread.start()
        # app.logger.info(form.data)
        crawl.crawler(form.data)      # Call function to perform crawl using the Form submissions on the the search routes

        # use make_response so we can set cookies
        # create response object with redirect to 'results' as action
        response = make_response(redirect(url_for('results', code=307)))

        # if a cookie is already set, append the new url to the cookie string
        if url_cookie:
            # TODO if url isn't already saved
            if form.starting_url.data not in url_cookie:

                # append url to cookie string with ", " delimiter
                url_cookie += ", " + form.starting_url.data
                response.set_cookie('urls', url_cookie) # set the new cookie

        # else, if no 'urls' cookie yet, set urls cookie to new url
        else:
            response.set_cookie('urls', form.starting_url.data)

        # set the cookie and redirect to results page
        return response

    # else if the user arrived via GET request from homepage
    else:

        url_list = None

        # if a cookie is set, send it as a list to the search template
        # to be rendered within dropdown input
        if url_cookie:
            url_list = url_cookie.split(delimiter)     # split into list
            # render_template('search.html', form=form, url_list=url_list) # render search.html with url_list

        # render the search form template
        return render_template('search.html', form=form, url_list=url_list)

# Routing for Search Results
@app.route('/results', methods=['GET', 'POST'])
def results():
    return render_template('results.html')

if __name__ == '__main__':
    app.debug = True      # FIXME remove when done debugging
    app.run(debug=True, port=7777, threaded=True)
