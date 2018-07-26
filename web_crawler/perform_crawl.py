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
** - https://pythonspot.com/extract-links-from-webpage-beautifulsoup/
** - https://stackoverflow.com/questions/1080411/retrieve-links-from-web-
**   page-using-python-and-beautifulsoup
** - https://stackoverflow.com/questions/1936466/beautifulsoup-grab-
**   visible-webpage-text
********************************************************************************
"""

import random                                                                   # Imports the python random library
import requests                                                                 # Import the requests python library to make HTML requests and download data
from bs4 import BeautifulSoup, SoupStrainer                                     # Import the BeautifulSoup library to navigate through HTML with Python
import send_data as send                                                        # Imports the code from the send_data.py file (uses send alias)

"""
********************************************************************************
* Description: start_search function
* Function calls either the breadth_first_search function or the
* depth_first_search function depending on the search state variable for search
* type.
********************************************************************************
"""

def start_search(state):
    if state.breadth_search == True:
        breadth_first_search(state, state.starting_url)
    if state.depth_search == True:
        depth_first_search(state, state.starting_url)

"""
********************************************************************************
* Description: breadth_first_search function
********************************************************************************
"""

def breadth_first_search(state, url):
    for x in range(state.depth):
        soup, url_list = search_urls(url)
        for y in range(len(url_list)):
            send.send_data_server(url, url_list, y)
            url = url_list[y]

"""
********************************************************************************
* Description: depth_first_search function
* Function begins with a url, collects all links on the page, store those
* results as a json file then begins again at another URL selected from the page
* at random.  This process continues until either the search depth limit is
* reached or the optional keyword is encountered.
********************************************************************************
"""

def depth_first_search(state, url):
    for x in range(state.depth):                                                # Continue searching pages until the search limit is reached
        soup, url_list = search_urls(url)                                       # Call function that will perform the web crawling functionality
        if state.keyword_used:                                                  # If the optional keyword is input by the user
            search_keyword(soup, state.keyword)
        send.send_data_server(url, url_list, x)                                 # Call function necessary for packaging and shipping the current page and it's URL connections
        url = select_random_url(url_list)


"""
********************************************************************************
* Description: search_urls function
* Function searches each webpage for all present URL Links.  Those links are
* stored to a list and returned to the calling function
********************************************************************************
"""

def search_urls(urls):                                                          # Set the first URL to the input provided in the command line
    soup = collect_page_details(urls)                                           # Call function to grab HTML information from the specified web page (Send the page)
    url_list = collect_links(urls, soup)                                        # Call function to collect Links (anchor tags) from pages
    return soup, url_list

"""
********************************************************************************
* Description: collect_page_details function
* Function uses the requests library to collect the HTML information from a
* webpage.  It next uses the BeautifulSoup library to parse the HTML information
* into a BeautifulSoup Object.  The BeautifulSoup Object is returned to the
* calling function.
********************************************************************************
"""

def collect_page_details(url):
    html_res = requests.get(url)                                                # Get the content from the current webpage and assign to variable
    soup = BeautifulSoup(html_res.text, "html.parser")                          # Parse the HTML text return from the res.text object (Return beautiful soup object)
    return soup                                                                 # Return the parsed BeautifulSoup object to the calling function

"""
********************************************************************************
* Description: collect_links function
* Function collects all URL Information that exists on the page and creates a
* list to be returned to the calling function.  If the URL does not begin with
* https or http (i.e. links on the /intl/en/policies/terms/ on google.com) then
* I append the full URL name to the beginning of the string before adding to
* returned list.
********************************************************************************
"""

def collect_links(url, soup):
    links = []                                                                  # Establish an empty list that will eventually hold the list of urls
    for anchor in soup.find_all('a', href=True):                                # Loop through each anchor tag found in the parsed BeautifulSoup Object
        # if not anchor.get('href').startswith("http"):                           # If the found URL does not begin with http or https
        #     page = url + anchor.get('href')                                     # Add the initial full URL name to the beginning of the string
        # else:                                                                   # Otherwise
        page = anchor.get('href')                                           # Just use the name that was found by the scraper
        links.append(page)                                                      # Append the URL link to the list
    return links                                                                # Return the URL links list to the calling function

"""
********************************************************************************
* Description: search_keyword function
* THIS FUNCTIONALITY WILL BE IMPLEMENTED NEXT WEEK
* ******* PRIORITY *******
********************************************************************************
"""

def search_keyword(soup, keyword):
    # texts = soup.find_all('h1',text=True)
    for node in soup.findAll('p'):
        text = ''.join(node.findAll(text=True))
    print(text)

"""
********************************************************************************
* Description: select_random_url function
* Function is used to select a URL from the list at random during depth first
* Web crawls
********************************************************************************
"""

def select_random_url(url_list):
    return(random.choice(url_list))                                             # Return a randomly selected URL from the list
