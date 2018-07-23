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
********************************************************************************
"""

import requests                                                                 # Import the requests python library to make HTML requests and download data
from bs4 import BeautifulSoup, SoupStrainer                                     # Import the BeautifulSoup library to navigate through HTML with Python

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
        if not anchor.get('href').startswith("http"):                           # If the found URL does not begin with http or https
            page = url + anchor.get('href')                                     # Add the initial full URL name to the beginning of the string
        else:                                                                   # Otherwise
            page = anchor.get('href')                                           # Just use the name that was found by the scraper
        links.append(page)                                                      # Append the URL link to the list
    return links                                                                # Return the URL links list to the calling function

"""
********************************************************************************
* Description: collect_names function
* NOT CURRENTLY USED.  MAY REMOVED IT FUNCTION PROVES UNNECESSARY
********************************************************************************
"""

def collect_names(links):
    link_names = []
    for link in links:
        print(a.find("a").get_text())
    return link_names

"""
********************************************************************************
* Description: search_keyword function
* THIS FUNCTIONALITY WILL BE IMPLEMENTED NEXT WEEK
* ******* PRIORITY *******
********************************************************************************
"""

def search_keyword(soup, keyword):
    print("Searching for keyword on page")
