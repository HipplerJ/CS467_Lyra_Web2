#!/usr/bin/python3

"""
********************************************************************************
** Authors:
** James Hippler (hipplerj@oregonstate.edu)
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
** Filename: crawler.py
**
** External Resources:
** - https://pythonspot.com/extract-links-from-webpage-beautifulsoup/
********************************************************************************
"""

import sys                                                                      # Imports the default sys python library
import search_state as ss                                                       # Imports the Class code from the search_state file
import perform_crawl as crawl                                                   # Imports the code from the perform_crawl.py file (uses crawl alias)

def crawler(url, method, depth, keyword):
    state = ss.search_state()                                                   # Instantiate the search_state Class Object
    state.initialize_state(url, method, depth, keyword)                         # Call search_state object function to initialize search parameters
    crawl.start_search(state)                                                   # Call the function to start the search
