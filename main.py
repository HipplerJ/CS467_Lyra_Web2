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

import os
import sys
sys.path.append('web_crawler/')                                                 # Add the python crawler directory to the system path
import threading
from flask import Flask, render_template, url_for, redirect, request, make_response
from wtforms import Form, StringField, IntegerField, RadioField, validators
import crawler as crawl
import validators


app = Flask(__name__)


# Routing for the Home (main) page
@app.route('/')
def index():
    return render_template('home.html')


# Form validator function: validates url and keyword
def url_validator(url):
    # Validate url
    if validators.domain(url) != True:
        # TODO Display error message
        # print("Invalid url")
        return False
    return True


def keyword_validator(keyword):
    # Validate keyword - check if is alphabetic
    if keyword.isalpha() != True and keyword != "":
        # print("Keyword must be alphabetic characters only")
        return False
    return True


# Routing for the Search Form Page
@app.route('/search', methods=['GET', 'POST'])
def search():

    # Check cookies to see if we have previously saved searches
    url_cookie = request.cookies.get('urls')

    # Check cookies for errors
    url_error = request.cookies.get('url_error')
    keyword_error = request.cookies.get('keyword_error')

    # Use this delimiter for urls when they're saved as a string
    delimiter = ", "

    # Post handler - if the user has posted data from the form to this url:
    if request.method == 'POST':

        # Get variables from the form
        url = request.form['starting_url']
        method = request.form['method']
        depth = request.form['depth']
        keyword = request.form['keyword']

        # FIXME Make form object to send to crawler??
        form_data = {'starting_url': url, 'method': method, 'depth':depth, 'keyword' : keyword}

        # Set url_error if url is invalid
        url_error = None
        # Set keyword_error if keyword is invalid
        keyword_error = None

        # Validate url
        if url_validator(url):

            # Validate keyword
            if keyword_validator(keyword):





                # FIXME Trace statements (DELETE)
                print("Starting url: %s" %url)
                print("Method: %s" %method)
                print("Depth: %s" %depth)
                print("Keyword: %s" %keyword)

                # Call crawler
                # crawler_thread = threading.Thread(target=crawl.crawler, args=form.data)
                # crawler_thread.start()
                # app.logger.info(form.data)
                # crawl.crawler(form.data)      # Call function to perform crawl using the Form submissions on the the search routes
                # crawl.crawler(form_data)

                # Use make_response to create response object so we can set cookies
                # Create response object that redirects to 'results' url
                response = make_response(redirect(url_for('results', code=307)))

                # If url history cookie is already set, append the new url to the cookie string
                if url_cookie:
                    if url not in url_cookie:
                        # FIXME append url to cookie string with ", " delimiter
                        url_cookie += ", " + url
                        response.set_cookie('urls', url_cookie)

                # Else, if no 'urls' cookie yet, create 'urls' cookie and add new url
                else:
                    response.set_cookie('urls', url)

                # TODO Since everything is valid, delete any url_error or keyword_error cookies
                response.set_cookie('url_error', '', expires=0)
                response.set_cookie('keyword_error', '', expires=0)

                # Set the cookie and redirect to the results page
                return response

            # Else if keyword is invalid, redirect back to search page and display keyword warning
            else:
                # Set error message to be displayed on search form
                keyword_error = "Invalid keyword submitted. Please enter a valid keyword (one word, alphabetic characters)"


                response = make_response(redirect(url_for('search')))
                # Set keyword error cookie
                response.set_cookie('keyword_error', keyword_error)
                # Remove url_error cookie since the url worked in this case
                response.set_cookie('url_error', '', expires=0)
                # Redirect back to this url '/search'
                return response


                # TODO Add error messaging (search takes error parameter error = None? then {$if error$} show the error?)
                # Render search form with error message (and cookies)
                # render_template('search.html', url_list=url_list, url_error=url_error, keyword_error=keyword_error)

        # TODO Else if url is not valid, redirect back to search page and display url error
        else:
            # Set error message to be displayed on search form
            url_error = "Invalid URL submitted. Please enter a valid URL"

            # TODO Add error messaging (search takes error parameter error = None? then {$if error$} show the error?)
            # Render search form with error message (and cookies)
            # render_template('search.html', url_list=url_list, url_error=url_error, keyword_error=keyword_error)

            # TODO Set url_error cookie and redirect to search (this) url
            response = make_response(redirect(url_for('search')))
            response.set_cookie('url_error', url_error)
            return response

    # Else if the user arrived via GET request from homepage, render the search form
    else:
        # Instantiate url_list, url_error, keyword_error to None
        url_list = None

        # Check for previously saved searches to save as list in url_list to be
        # used in dropdown input form
        if url_cookie:
            # Split into list to send to template
            url_list = url_cookie.split(delimiter)

        # Render the search form template with either a list of url's or nothing
        return render_template('search.html', url_list=url_list, url_error=url_error, keyword_error=keyword_error)

# Routing for Search Results
@app.route('/results', methods=['GET', 'POST'])
def results():
    return render_template('results.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True, port=7777, threaded=True)
