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
import random                                                                   # Imports the python random library
import search_state as search                                                   # Imports the Class code from the search_state file (uses search as alias)
import check_arguments as conf                                                  # Imports the code from the check_arguments.py file (uses conf alias)
import perform_crawl as crawl                                                   # Imports the code from the perform_crawl.py file (uses crawl alias)
import send_data as send                                                        # Imports the code from the send_data.py file (uses send alias)

# """
# ********************************************************************************
# * Description: confirm_keyword function
# * Function is used to confirm that the optional keyword was implemented by the
# * user and that the keyword is valid.
# ********************************************************************************
# """
#
# def confirm_keyword():
#     if len(sys.argv) == 5:                                                      # If user input 5 arguments, use the forth array element (5th Argument) as the keyword
#         return True                                                             # Return true indicating that the optional keyword exists
#     else:                                                                       # Otherwise, if only four arguments were issued
#         return False                                                            # Return False indicating that the optional keyword was not used

"""
********************************************************************************
* Description: search_urls function
* Function searches each webpage for all present URL Links.  Those links are
* stored to a list and returned to the calling function
********************************************************************************
"""

def search_urls(urls):                                                          # Set the first URL to the input provided in the command line
    soup = crawl.collect_page_details(urls)                                     # Call function to grab HTML information from the specified web page (Send the page)
    url_list = crawl.collect_links(urls, soup)                                  # Call function to collect Links (anchor tags) from pages
    return url_list

"""
********************************************************************************
* Description: bfs function
* STILL NEEDS TO BE IMPLEMENTED.  BREADTH FIRST IS NOT
********************************************************************************
"""

def bfs(start_url, search_limit, keyword_used):
    for x in range(search_limit):
        url_list = search_urls(start_url)
        for url in url_list:
            # if keyword_used:                                                  # If the optional keyword is input by the user
            #     keyword = sys.argv[4]                                         # Set the optional keyword to the value provided on the command line when the program was started
            #     keyword_found = search_keyword()                              # Search for keyword on the current page and end the process if found
            send_data_server(start_url, url_list)                               # Call function necessary for packaging and shipping the current page and it's URL connections
            start_url = url_list[url]

"""
********************************************************************************
* Description: dfs function
* Function begins with a url, collects all links on the page, store those
* results as a json file then begins again at another URL selected from the page
* at random.  This process continues until either the search depth limit is
* reached or the optional keyword is encountered
********************************************************************************
"""

def dfs(start_url, search_limit, keyword_used):
    for x in range(search_limit):                                               # Continue searching pages until the search limit is reached
        url_list = search_urls(start_url)                                       # Call function that will perform the web crawling functionality
        # if keyword_used:                                                      # If the optional keyword is input by the user
        #     keyword = sys.argv[4]                                             # Set the optional keyword to the value provided on the command line when the program was started
        #     keyword_found = search_keyword()                                  # Search for keyword on the current page and end the process if found
        send_data_server(start_url, url_list, x)                                # Call function necessary for packaging and shipping the current page and it's URL connections
        start_url = select_random_url(url_list)

"""
********************************************************************************
* Description: send_data_server function
* Function that packages and writes the URL graphs.  Write each node as they
* become available in order to stream data.
********************************************************************************
"""

def send_data_server(start_url, url_list, depth):
    data = send.package_content(start_url, url_list)                            # Create the dictionary (graph) relationship between the node and it's URLS
    send.write_json(data, depth)                                                # Write the information to a .json file

"""
********************************************************************************
* Description: select_random_url function
* Function is used to select a URL from the list at random during depth first
* Web crawls
********************************************************************************
"""

def select_random_url(url_list):
    return(random.choice(url_list))                                             # Return a randomly selected URL from the list

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
    conf.confirm_total(sys.argv)                                                # Confirms that the user input the appropriate number of arguments
    conf.confirm_url(sys.argv[1])                                               # Confirms that a valid starting URL was provided by the user
    conf.confirm_search_type(sys.argv[2])                                       # Confirms that the user input a valid search type (breadth or depth)
    conf.confirm_limit(sys.argv[3])                                             # Confirms that the user input a numeric value as the search limit

"""
********************************************************************************
* Description: main function
* Main function is used to orchestrate the crawler program and call function in
* the appropriate order.
********************************************************************************
"""

def main():
    state = search.search_state()                                               # Instantiate the search_state Object
    state.initialize_state(sys.argv)                                            # Call search_state object function to initialize search parameters

    # # confirm_standard_input()                                                  # Call function to confirm provided arguments are valid
    # start_url = sys.argv[1]                                                     # Set the starting URL to the value provided on the command line when the program was started
    # search_limit = int(sys.argv[3])                                             # Set the search limit to the value provided on the command line when the program was started
    # keyword_used = confirm_keyword()                                            # Call function to confirm keyword input (if exists) and store returned boolean variable
    # if sys.argv[2] == "breadth":                                                # If Search option Breadth-First was selected
    #     dfs(start_url, search_limit, keyword_used)                              # Call the appropriate function to perform BFS
    # if sys.argv[2] == "depth":                                                  # If Search option Depth-First was selected
    #     dfs(start_url, search_limit, keyword_used)                              # Call the appropriate function to perform DFS

if __name__ == '__main__':                                                      # Initialize the main function in Python
    main()                                                                      # Call main function and begin the program
