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
** - https://stackoverflow.com/questions/8634473/sending-json-request-with-
**   python
** - http://docs.python-requests.org/en/latest/user/advanced/#event-hooks
********************************************************************************
"""

import json                                                                     # Import the library necessary for exporting data to a json file
import os                                                                       # Import the os library necessary for checking and creating directories

"""
********************************************************************************
* Description: write_json_file function
* Function stores each nodes and it's connections as an individual .json file
* under a directory called crawler_results located in the project.  If the
* directory does not previously exist, then it is created.
********************************************************************************
"""

def write_json_file(data):
    dir_name = "static/json/crawler_results"                                    # Store results in a directory called crawler_results in the parent project folder
    file_name = "{}/results.json".format(dir_name)                              # Set the filename to ../crawler_results/results_page_[x].json
    if not os.path.exists(dir_name):                                            # Check for a directory called crawler_results in the project folder
        os.makedirs(dir_name)                                                   # If it does not exist, then create the directory
    with open(file_name, 'w') as file_out:                                      # Open a json file and dump the current graph with the appropriate json formatting
        json.dump(data, file_out)
