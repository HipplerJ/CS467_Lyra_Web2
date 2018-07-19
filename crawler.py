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
import check_arguments as conf                                                  # Imports the code from the check_arguments.py file (uses conf alias)
import perform_crawl as crawl                                                   # Imports the code from the perform_crawl.py file (uses conf crawl)
import send_data as send

"""
********************************************************************************
* Description: confirm_keyword function
* Function is used to confirm that the optional keyword was implemented by the
* user and that the keyword is valid.
********************************************************************************
"""

def confirm_keyword():
    if len(sys.argv) == 5:                                                      # If user input 5 arguments, use the forth array element (5th Argument) as the keyword
        return True                                                             # Return true indicating that the optional keyword exists
    else:                                                                       # Otherwise, if only four arguments were issued
        return False                                                            # Return False indicating that the optional keyword was not used

"""
********************************************************************************
* Description: web_crawler function
********************************************************************************
"""

def web_crawler(keyword_used):
    soup = crawl.parse_html(sys.argv[1])                                        # Call function to grab HTML information from the specified web page (Send the page)
    url_list = crawl.scrape_urls(soup)                                          # Call function to collect Links (anchor tags) from pages
    link_names = crawl.collect_names(soup)
    print(url_list)
    # if keyword_used:                                                            # If the user decided to implement a keyword search
    #     crawl.search_keyword(soup, sys.argv[4])                                 # Call function to search the page for the specified keyword
    # send.write_json(urls_list)
    # initiate_search()                                                         # Call function to begin searching (breadth or depth first)

"""
********************************************************************************
* Description: confirm_input function
* Function is used to call functionins in the check_arguments.py file to confirm
* that the appropriate arguments are provided to the program upon execution.  It
* confirms the arguments total, the search type (breadth or depth), the search
* limit (verify numeric), and the keyword (string with no spaces).  Most of this
* functionality will already be performed by the web front end of the
* application
********************************************************************************
"""

def confirm_standard_input():
    conf.print_arguments(sys.argv)                                              # Prints the arguments to the console (used for testing)
#     conf.confirm_total(sys.argv)                                                # Confirms that the user input the appropriate number of arguments
#     conf.confirm_url(sys.argv[1])                                               # Confirms that a valid starting URL was provided by the user
#     conf.confirm_search_type(sys.argv[2])                                       # Confirms that the user input a valid search type (breadth or depth)
#     conf.confirm_limit(sys.argv[3])                                             # Confirms that the user input a numeric value as the search limit

"""
********************************************************************************
* Description: initiate_search function
********************************************************************************
"""

def initiate_search():
    if sys.argv[2] == "breadth":                                                # If Search option Breadth-First was selected
        bfs.BFS(sys.argv)                                                       # Call the appropriate function to perform BFS
    if sys.argv[2] == "depth":                                                  # If Search option Depth-First was selected
        dfs.DFS(sys.argv)                                                       # Call the appropriate function to perform DFS

"""
********************************************************************************
* Description: main function
* Main function is used to orchestrate the crawler program and call function in
* the appropriate order.
********************************************************************************
"""

def main():
    confirm_standard_input()                                                    # Call function to confirm provided arguments are valid
    keyword_used = confirm_keyword()                                            # Call function to confirm keyword input (if exists) and store returned boolean variable
    web_crawler(keyword_used)                                                   # Call function that will perform the web crawling functionality

if __name__ == '__main__':                                                      # Initialize the main function in Python
    main()                                                                      # Call main function and begin the program
