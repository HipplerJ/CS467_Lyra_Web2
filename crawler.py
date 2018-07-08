
#!/usr/bin/python

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
********************************************************************************
"""

import sys

"""
********************************************************************************
* Description: print_arguments function
********************************************************************************
"""

def print_arguments():
    print("{} arguments provided on command line".format(len(sys.argv)))
    for x in range(len(sys.argv)):
        print("Argument {}: {}".format(x, sys.argv[x]))

"""
********************************************************************************
* Description: check_argument_total function
********************************************************************************
"""

def check_argument_total():
    if len(sys.argv) < 3:
        print("Too few arguments")
    elif len(sys.argv) > 3:
        print("Too many arguments")
    else:
        print("Correct number of arguments")

"""
********************************************************************************
* Description: main function
********************************************************************************
"""

def main():
    print_arguments()
    check_argument_total()

if __name__ == '__main__':
    main()
