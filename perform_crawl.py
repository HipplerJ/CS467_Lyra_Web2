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
* Description: parse_html function
********************************************************************************
"""

def parse_html(webpage):
    soup = collect_page_details(webpage)                                        # Call function to parse all HTML information from the specified URL
    return soup                                                                 # Return the HTML information to the calling function

"""
********************************************************************************
* Description: collect_page_details function
********************************************************************************
"""
def collect_page_details(url):
    res = requests.get(url)                                                     # Get the content from the current webpage and assign to variable
    soup = BeautifulSoup(res.text, "html.parser")                               # Parse the HTML text return from the res.text object (Return beautiful soup object)
    return soup

"""
********************************************************************************
* Description: scrape_urls function
********************************************************************************
"""

def scrape_urls(soup):
    url_list = collect_links(soup)                                              # Scrape all links from a provided website
    return url_list                                                             # Return the list of URLs (anchor tags that were found on the page)

"""
********************************************************************************
* Description: collect_links function
********************************************************************************
"""

def collect_links(soup):
    links = []
    for link in soup.find_all('a'):                                             # Find all anchor tags in the webpage and return to calling function
        links.append(link.get('href'))
    return(links)

"""
********************************************************************************
* Description: collect_names function
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
********************************************************************************
"""

def search_keyword(soup, keyword):
    print("Searching for keyword on page")

"""
********************************************************************************
* Description: print_links function
********************************************************************************
"""

def print_links(links):
    for x in range(len(links)):
        print(links[x])
