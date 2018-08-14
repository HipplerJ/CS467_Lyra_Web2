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

import send_data as send                                                        # Imports the code from the send_data.py file (uses send alias)
import graph as g                                                               # Imports the code from the graph.py file (uses g alias)
from random import choice                                                       # Imports the python random library
import requests                                                                 # Import the requests python library to make HTML requests and download data
from bs4 import BeautifulSoup                                                   # Import the BeautifulSoup library to navigate through HTML with Python
import re
import traversed as t

"""
********************************************************************************
* Description: start_search function
* Function calls either the breadth_first_search function or the
* depth_first_search function depending on the search state variable for search
* type.
********************************************************************************
"""

def start_search(state):
    graph = g.build_graph()                                                     # Create an instance of the graph class
    travel = t.Traversed()
    if state.breadth_search:                                                    # If Breadth First Search was Specified
        breadth_first_search(state, graph, travel, state.starting_url)          # Initiate Breadth First Search
    if state.depth_search:                                                      # If Depth First Search was Specified
        depth_first_search(state, graph, travel, state.starting_url)            # Initiate Depth First Search

"""
********************************************************************************
* Description: breadth_first_search function
********************************************************************************
"""

def breadth_first_search(state, graph, url):
    graph = g.build_graph()                                                     # Create an instance of the graph class
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

def depth_first_search(state, graph, travel, url):
    found = False                                                               # Establish a boolean variable to be used when looking for edges
    while len(travel.visited) <= state.depth:                                   # Perform the crawl until we've reached the depth specified by the user
        print("PLACES WE'VE BEEN")
        print(travel.visited)
        soup = visit_page(travel, url)
        if soup:                                                                # If the url was valid and the page content could be stored
            title, edge_list = get_page_details(travel, url, soup)
            if edge_list:                                                       # If the edge list had entries
                print("{} - GOOD TO GO".format(url))
                good_node(graph, title, url)                                           # Add the node as a regular entry to Arbor.js
                url = select_random_url(travel.map[travel.peek()], travel.visited)              # Select a new url at random from the list of links on the page
                graph.add_edges(travel.peek(), url)                             # Add a connection between the current node
            else:                                                       # If the edge list is empty and no links were found on the page
                print("{} - NO LINKS".format(url))
                no_links_node(graph, title, url) # Add the node to Arbor.js graph with the color orange
                if travel.size() == 1:
                    graph.add_edges(travel.peek(), '')
                    break
                prev_url = travel.pop()
                graph.add_edges(travel.peek(), prev_url)
                url = select_random_url(travel.map[travel.peek()], travel.visited)
                graph.add_edges(travel.peek(), url)                             # Add a connection between the current node
        else:
            print("{} - BAD LINK".format(url))
            invalid_url(graph, url)
            if travel.size() == 1:
                graph.add_edges(travel.peek(), '')
                break
            prev_url = travel.pop()
            graph.add_edges(travel.peek(), prev_url)
            url = select_random_url(travel.map[travel.peek()], travel.visited)
            graph.add_edges(travel.peek(), url)
    send_payload(graph)

"""
********************************************************************************
* Description: visit_page function
********************************************************************************
"""

def visit_page(travel, url):
    travel.push(url)                                                            # Add the URL to the visited list so that we can track that we've been there
    travel.visited.append(url)                                                  # Add the node to the list of visited websites so that we don't return
    soup = get_html(url)                                                        # Graph URL HTML information and parse as BeautifulSoup Object
    return soup

"""
********************************************************************************
* Description: get_page_details function
********************************************************************************
"""

def get_page_details(travel, url, soup):
    node_title = get_title(url, soup)                                           # Attempt to collect the title of the Web Page (if not found the Url is returned as the tite)
    edge_list = search_urls(soup, url)                                          # Check for Links on the page (For Exception Handling, only HTTP and HTTPS Links are collected)
    travel.map[url].extend(edge_list)                                           # Add the URL Edges to the traversal map
    return node_title, edge_list

"""
********************************************************************************
* Description: get_html function
********************************************************************************
"""

def get_html(url):
    try:
        html_res = requests.get(url)                                            # Get the content from the current webpage and assign to variable
        soup = BeautifulSoup(html_res.text, 'html.parser')                      # Parse the HTML text return from the res.text object (Return beautiful soup object)
        return soup
    except:
        return False

"""
********************************************************************************
* Description: get_title function
********************************************************************************
"""

def get_title(url, soup):
    try:
        return soup.title.string.strip()                                        # Return page title with leading and trailing spaces removed
    except:
        return "{} (Title Not Found)".format(url)

"""
********************************************************************************
* Description: search_urls function
* Function searches each webpage for all present URL Links.  Those links are
* stored to a list and returned to the calling function
********************************************************************************
"""

def search_urls(soup, urls):                                                    # Set the first URL to the input provided in the command line
    links = []                                                                  # Establish an empty list that will eventually hold the list of urls
    for anchor in soup.find_all('a', href=True):                                # Loop through each anchor tag found in the parsed BeautifulSoup Object
        if anchor.get('href').startswith("http"):                               # If the found URL does not begin with http or https, Ignore it (TRY TO FIX THIS LATER)
            links.append(anchor.get('href'))                                    # Append the URL link to the list
    return links                                                                # Return the URL links list to the calling function

"""
********************************************************************************
* Description: search_keyword function
********************************************************************************
"""

def search_keyword(soup, keyword):
    results = soup.body.find_all(string=re.compile('.*{0}.*'.format(keyword)), recursive=True)
    print('Found the word "{0}" {1} times\n'.format(keyword, len(results)))

    for content in results:
        words = content.split()
        for index, word in enumerate(words):
            # If the content contains the search word twice or more this will fire for each occurence
            if word == keyword:
                print('Whole content: "{0}"'.format(content))
                before = None
                after = None
                # Check if it's a first word
                if index != 0:
                    before = words[index-1]
                # Check if it's a last word
                if index != len(words)-1:
                    after = words[index+1]
                print('\tWord before: "{0}", word after: "{1}"'.format(before, after))

"""
********************************************************************************
* Description: select_random_url function
* Function is used to select a URL from the list at random during depth first
* Web crawls
********************************************************************************
"""

def select_random_url(url_list, visited):
    found = False
    while not found:
        random = choice(url_list)
        if random not in visited:
            found = True
    return random

"""
********************************************************************************
* Description: good_node function
********************************************************************************
"""

def good_node(graph, title, url):
    build_nodes(graph, title, url, '#B0BEC5')

"""
********************************************************************************
* Description: no_links_node function
********************************************************************************
"""

def no_links_node(graph, title, url):
    build_nodes(graph, "{} (No Links On Page)".format(title), url, '#FF7043')

"""
********************************************************************************
* Description: invalid_url function
********************************************************************************
"""

def invalid_url(graph, url):
    build_nodes(graph, "{} (Invalid URL)".format(url), url, '#E53935')

"""
********************************************************************************
* Description: build_nodes function
********************************************************************************
"""

def build_nodes(graph, title, url, color):
    graph.add_nodes(title, url, color)

"""
********************************************************************************
* Description: send_payload function
********************************************************************************
"""

def send_payload(graph):
    graph.package_graph()
    send.write_json_file(graph.graph)
    reset_graph(graph)

"""
********************************************************************************
* Description: reset_graph function
********************************************************************************
"""

def reset_graph(graph):
    graph.visited = []
    graph.nodes = {}
    graph.edges = {}
    del graph
