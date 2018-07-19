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
** Filename: perform_crawl.py
**
** External Resources:
** - https://stackoverflow.com/questions/12309269/how-do-i-write-json-data-to-
**   a-file
********************************************************************************
"""

import json                                                                     # Import the library necessary for exporting data to a json file

"""
********************************************************************************
* Description: write_json function
********************************************************************************
"""

def write_json(data):
    with open('results.json', 'w') as out_file:
        json.dump(data, out_file)
