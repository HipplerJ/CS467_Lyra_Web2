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
    if state.breadth_search:                                                    # If Breadth First Search was Specified
        breadth_first_search(state, graph, state.starting_url)                  # Initiate Breadth First Search
    if state.depth_search:                                                      # If Depth First Search was Specified
        depth_first_search(state, graph, state.starting_url)                    # Initiate Depth First Search

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

def depth_first_search(state, graph, url):
    last_edges = []
    x = 0
    while x < state.depth:
    # for x in range(state.depth):                                              # Loop through the search process for the search depth specified by the user
        add_to_visited(graph, url)                                              # Add the node to the visited url list so that we don't repeat
        soup = get_page(url)                                                    # Collect HTML from Page and Parse into BeautifulSoup Object
        if soup:                                                                # If the page can be found (valid URL)
            node = get_title(url, soup)                                         # Collect the page Title
            edge_list = search_urls(soup, url)                                  # Collect All http and https URLs on the page
            if edge_list:
                last = url
                last_edges = edge_list
                build_nodes(graph, node, url, '#B0BEC5')
                url = select_random_url(edge_list, graph)
                build_edge_connections(graph, last, url)
                x += 1
            else:
                build_nodes(graph, "{} (No Links On Page)".format(node), url, '#FF7043')    # Make color Orange
                build_edge_connections(graph, last, url)
                if x == 0:                                                      # If this is the starting URL
                    break                                                       # Break the cycle because there are no links to follow
                else:
                    url = select_random_url(last_edges, graph)
                    continue
        else:
            build_nodes(graph, "Invalid URL", url, '#E53935')                   # Make color red
            if x == 0:                                                          # If this is the starting URL
                break                                                           # Break the cycle because page cannot be loaded
            else:
                continue
            x += 1
    graph.package_graph()
    send.write_json_file(graph.graph)
    reset_graph(graph)                                                          # Ensures that the graph class objects are deleted once complete (Get weird errors if not)

"""
********************************************************************************
* Description: build_nodes function
********************************************************************************
"""

def add_to_visited(graph, url):
    graph.visited.append(url)

"""
********************************************************************************
* Description: build_nodes function
********************************************************************************
"""

def build_nodes(graph, node, link, color):
    print(node)
    print(link)
    graph.add_nodes(node, link, color)

"""
********************************************************************************
* Description: build_connections function
********************************************************************************
"""

def build_edge_connections(graph, node, connection):
    graph.add_edges(node, connection)

"""
********************************************************************************
* Description: get_page function
********************************************************************************
"""

def get_page(url):
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
        return "Page Title Not Found"
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

def select_random_url(url_list, graph):
    print(graph.visited)
    random = choice(url_list)                                                   # Return a randomly selected URL from the list
    if random in graph.visited:
        select_random_url(url_list, graph)
    return random

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
