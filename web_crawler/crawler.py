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

"""
********************************************************************************
* Description: main function
* Main function is used to orchestrate the crawler program and call function in
* the appropriate order.
********************************************************************************
"""

def main():
    state = ss.search_state()                                                   # Instantiate the search_state Class Object
    state.initialize_state(sys.argv)                                            # Call search_state object function to initialize search parameters
    crawl.start_search(state)

if __name__ == '__main__':                                                      # Initialize the main function in Python
    main()                                                                      # Call main function and begin the program
