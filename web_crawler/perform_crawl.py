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
import graph as g
from random import choice                                                       # Imports the python random library
import requests                                                                 # Import the requests python library to make HTML requests and download data
from bs4 import BeautifulSoup                                                   # Import the BeautifulSoup library to navigate through HTML with Python

"""
********************************************************************************
* Description: start_search function
* Function calls either the breadth_first_search function or the
* depth_first_search function depending on the search state variable for search
* type.
********************************************************************************
"""

def start_search(state):
    if state.breadth_search:
        breadth_first_search(state, state.starting_url)                         # Initiate Breadth First Search
    if state.depth_search:
        depth_first_search(state, state.starting_url)                           # Initiate Depth First Search

"""
********************************************************************************
* Description: breadth_first_search function
********************************************************************************
"""

def breadth_first_search(state, url, url_list):
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
    graph = g.build_graph()                                                     # Create an instance of the graph class
    for x in range(state.depth):                                                # Loop through the search process for the search depth specified by the user
        soup = get_page(url)                                                    # Collect HTML from Page and Parse into BeautifulSoup Object
        if soup:
            node = get_title(url, soup)                                         # Collect the page Title
            edge_list = search_urls(soup, url)                                  # Collect All http and https URLs on the page
            build_node_info(graph, node, url)                                          # Add the node to the visited url list so that we don't repeat
            build_nodes_connections(graph, node, url)
            url = select_random_url(edge_list, graph)
            if not url:
                break
        # else:
        #     graph.add_nodes("Page Not Found", url)
        #     if x == 0:
        #         break                                                         # Break the cycle because page cannot be loaded
    build_edge_connections(graph)
    graph.package_graph()
    send.write_json_file(graph.graph)
    print(graph.visited)
    print(graph.nodes)
    print(graph.edges)
    del graph                                                                   # Ensures that the graph class objects are deleted once complete (Get weird errors if not)

"""
********************************************************************************
* Description: build_nodes function
********************************************************************************
"""

def build_node_info(graph, node, link):
    node_info = []
    node_info.append(node)
    node_info.append(link)
    graph.visited.append(node_info)

"""
********************************************************************************
* Description: build_nodes function
********************************************************************************
"""

def build_nodes_connections(graph, node, link):
    graph.add_nodes(node, link)

"""
********************************************************************************
* Description: build_connections function
********************************************************************************
"""

def build_edge_connections(graph):
    for x in range(len(graph.visited) - 1):
        graph.add_edges(graph.visited[x][0], graph.visited[x + 1][0])

# def depth_first_search(state, url):
#     graph = g.build_graph()
#     for x in range(state.depth):
#         graph.visited.append(url)
#         soup = get_page(url)                                                    # Collect HTML from Page and Parse into BeautifulSoup Object
#         node = get_title(url, soup)                                             # Collect the page Title
#         edge_list = search_urls(soup, url)                                      # Collect All http and https URLs on the page
#         print(edge_list)
#         graph.add_nodes(node, url)
#         build_connections(graph, node, edge_list)
#         url = select_random_url(edge_list, graph)
#     graph.package_graph()
#     send.write_json_file(graph.graph)



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
        return "No Title Found"
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
* THIS FUNCTIONALITY WILL BE IMPLEMENTED NEXT WEEK
* ******* PRIORITY *******
********************************************************************************
"""

def search_keyword(soup, keyword):
    # texts = soup.find_all('h1',text=True)
    for node in soup.findAll('p'):
        text = ''.join(node.findAll(text=True))
    print(text)

        # if state.keyword_used:                                                # If the optional keyword is input by the user
        #     search_keyword(soup, state.keyword)

"""
********************************************************************************
* Description: select_random_url function
* Function is used to select a URL from the list at random during depth first
* Web crawls
********************************************************************************
"""

def select_random_url(url_list, graph):
    try:
        random = choice(url_list)                                               # Return a randomly selected URL from the list
    except:
        return False
    if random in graph.visited:
        select_random_url(url_list, graph)
    return random
