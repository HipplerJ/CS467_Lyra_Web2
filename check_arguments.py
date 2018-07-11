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
** Filename: check_arguments.py
********************************************************************************
"""

"""
********************************************************************************
* Description: print_arguments function
********************************************************************************
"""

def print_arguments(arguments):
    print("{} arguments provided on command line".format(len(arguments)))
    for x in range(len(arguments)):
        print("Argument {}: {}".format((x + 1), arguments[x]))

"""
********************************************************************************
* Description: check_argument_total function
********************************************************************************
"""

def confirm_total(arguments):
    if len(arguments) < 4:
        print("Too few arguments")
        exit(1)
    elif len(arguments) > 5:
        print("Too many arguments")
        exit(1)
    else:
        print("Correct number of arguments")

"""
********************************************************************************
* Description: confirm_search_type function
********************************************************************************
"""

def confirm_url(url):
    print("Starting URL: {}".format(url))
    print("Need to implement URL validation")

"""
********************************************************************************
* Description: confirm_search_type function
********************************************************************************
"""

def confirm_search_type(search_type):
    print("Search Type: {}".format(search_type))
    if search_type != "breadth" and search_type != "depth":
        print("Search type is not valid")
        print("Search type must be breadth-first or depth-first")
        exit(1)
    else:
        if search_type == 'breadth':
            search = "Breadth-First"
        else:
            search = "Depth-First"
        print("Using {} Search Method".format(search))

"""
********************************************************************************
* Description: confirm_limit function
********************************************************************************
"""

def confirm_limit(number):
    print("Search Limit: {}".format(number))
    try:
        limit = int(number)
    except ValueError:
        print("Search Limit needs to be a numeric value")
        exit(1)
    if int(number) <= 0:
        print("Search Limit needs to be a positive numeric value")
        exit(1)

"""
********************************************************************************
* Description: confirm_keyword function
********************************************************************************
"""

def confirm_keyword(keyword):
    print("Keyword: {}".format(keyword))
    print("Need to implement keyword confirmation")
