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

    # print("form.validate: " + str(form.validate()))
    # if request.method == 'POST' and form.validate():
    if request.method == 'POST':

        # crawler_thread = threading.Thread(target=crawl.crawler, args=form.data)
        # crawler_thread.start()
        # app.logger.info(form.data)
        # crawl.crawler(form.data)                                                # Call function to perform crawl using the Form submissions on the the search routes

        # TODO get previous cookie starting_page_list of starting page:keyword object.
        # TODO if the starting webpage/keyword combo is not in the list returned by the cookie
            # TODO add the starting webpage/keyword combo to the cookie list
                # TODO if no keyword entered, add ""
        # TODO set the cookie with the new list (with new start_page_url/keyword appended to it)



        # TODO save searched web page and associated keyword to cookie
        # response = make_response(redirect(url_for('results',data=request.form.get("data")),code=307))
        # response = make_response(redirect(url_for('results',data='hi does this work'),code=307))
        # stuff = "works?"
        # response = make_response(redirect(url_for('results',form_data=stuff)))


        # FIXME trace statements
        # for item in form:
        #     print("%s: %s" %(item.name, item.data))
        # print(str(form))

        # TODO make redirect work ... for the FIRST time
        # return redirect(url_for('results',data=request.form.get("data")),code=307)
        # return redirect(url_for('results', data=form))
        # return redirect(url_for('index'))
        # return response
        return render_template('results.html', form=form)


    # TODO if its a get request, check for cookie.
    # If cookie exists, print the list of previous starting pages/keywords when rendering template
    return render_template('search.html', form=form)

# Routing for Search Results
@app.route('/results/<data>', methods=['GET', 'POST'])
def results(data):
    return render_template('results.html', data=data)

if __name__ == '__main__':
    app.debug = True      # FIXME remove when done debugging
    app.run(debug=True, port=7777, threaded=True)
