
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

import sys                                                                      # Imports the default sys python library
import check_arguments as conf                                                  # Imports the code from the check_arguments.py file (uses conf alias)

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

def confirm_input():
    conf.print_arguments(sys.argv)                                              # Prints the arguments to the console (used for testing)
    conf.confirm_total(sys.argv)                                                # Confirms that the user input the appropriate number of arguments
    conf.confirm_url(sys.argv[1])                                               # Confirms that a valid starting URL was provided by the user
    conf.confirm_search_type(sys.argv[2])                                       # Confirms that the user input a valid search type (breadth or depth)
    conf.confirm_limit(sys.argv[3])                                             # Confirms that the user input a numeric value as the search limit
    conf.confirm_keyword(sys.argv[4])                                           # Confirms that the user input a single string keyword (no spaces)

"""
********************************************************************************
* Description: main function
* Main function is used to orchestrate the crawler program and call function in
* the appropriate order.
********************************************************************************
"""

def main():
    confirm_input()

if __name__ == '__main__':
    main()
