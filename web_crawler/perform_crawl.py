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
import depth_traversed as dt
from collections import defaultdict

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
    dt_travel = dt.Stack()
    if state.breadth_search:                                                    # If Breadth First Search was Specified
        breadth_first_search(state, graph, state.starting_url)                  # Initiate Breadth First Search
    if state.depth_search:                                                      # If Depth First Search was Specified
        depth_first_search(state, graph, dt_travel, state.starting_url)         # Initiate Depth First Search

"""
********************************************************************************
* Description: breadth_first_search function
********************************************************************************
"""

def breadth_first_search(state, graph, url):
    current_level = [url]
    next_level = []
    depth = 0
    while depth <= state.depth:
        for x in range(len(current_level)):
            soup = get_html(current_level[x])                                   # Graph URL HTML information and parse as BeautifulSoup Object
            if soup:
                title = get_title(current_level[x], soup)
                edge_list = search_urls(soup, current_level[x])
                if state.keyword_used:
                    search_keyword(state, soup, state.keyword)
                    if state.keyword_found:
                        keyword_node(graph, title, url, state)
                        break
                if edge_list:
                    good_node(graph, title, current_level[x], state)
                    next_level.extend(edge_list)
                    if depth < state.depth:
                        for y in range(len(edge_list)):
                            good_node(graph, edge_list[y], edge_list[y], state)
                            graph.add_edges(current_level[x],edge_list[y])
                else:
                    no_links_node(graph, title, current_level[x], state)
            else:
                invalid_url(graph, current_level[x])
        current_level = next_level
        next_level = []
        depth += 1
    send_payload(graph)

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
    while len(travel.visited) <= state.depth:                                   # Perform the crawl until we've reached the depth specified by the user
        soup = visit_page_depth(travel, url)
        if soup:                                                                # If the url was valid and the page content could be stored
            title, edge_list = get_page_details(travel, url, soup)
            if state.keyword_used:
                search_keyword(state, soup, state.keyword)
                if state.keyword_found:
                    keyword_node(graph, title, url, state)
                    break
            if edge_list:                                                       # If the edge list had entries
                good_node(graph, title, url, state)                             # Add the node as a regular entry to Arbor.js
                url = get_next_node(travel, graph, url)
            else:                                                               # If the edge list is empty and no links were found on the page
                no_links_node(graph, title, url, state)                         # Add the node to Arbor.js graph with the color orange
                if travel.size() == 1:
                    graph.add_edges(travel.peek(), '')
                    break
                prev_url = travel.pop()
                graph.add_edges(travel.peek(), prev_url)
                url = get_next_node(travel, graph, url)
        else:
            invalid_url(graph, url, state)
            if travel.size() == 1:
                graph.add_edges(travel.peek(), '')
                break
            prev_url = travel.pop()
            graph.add_edges(travel.peek(), prev_url)
            url = get_next_node(travel, graph, url)
    send_payload(graph)

"""
********************************************************************************
* Description: visit_page_depth function
********************************************************************************
"""

def visit_page_depth(travel, url):
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

def search_keyword(state, soup, keyword):
    if soup.body:
        results = soup.body.find_all(string=re.compile('.*{0}.*'.format(keyword)), recursive=True)
        if len(results) > 0:
            state.keyword_found = True

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
* Description: get_next_node function
********************************************************************************
"""

def get_next_node(travel, graph, url):
    url = select_random_url(travel.map[travel.peek()], travel.visited)          # Select a new url at random from the list of links on the page
    graph.add_edges(travel.peek(), url)
    return url

"""
********************************************************************************
* Description: good_node function
********************************************************************************
"""

def good_node(graph, title, url, state):
    build_nodes(graph, title, url, '#B0BEC5', state)

"""
********************************************************************************
* Description: keyword_node function
********************************************************************************
"""

def keyword_node(graph, title, url, state):
    build_nodes(graph, '{} - Keyword Found'.format(title), url, '#FFFF8D', state)

"""
********************************************************************************
* Description: no_links_node function
********************************************************************************
"""

def no_links_node(graph, title, url, state):
    build_nodes(graph, "{} (No Links On Page)".format(title), url, '#FF7043', state)

"""
********************************************************************************
* Description: invalid_url function
********************************************************************************
"""

def invalid_url(graph, url, state):
    build_nodes(graph, "{} (Invalid URL)".format(url), url, '#E53935', state)

"""
********************************************************************************
* Description: build_nodes function
********************************************************************************
"""

def build_nodes(graph, title, url, color, state):
    graph.add_nodes(title, url, color, state.keyword_found, state.keyword)

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
