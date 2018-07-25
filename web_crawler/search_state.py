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
** Filename: search_state.py
********************************************************************************
"""

"""
********************************************************************************
* Class Description: search_state CLASS
********************************************************************************
"""

class search_state():
    num_arguments = None
    starting_url = None                                                         # Create variable for the starting URL (Initialize to None)
    breadth_search = None                                                       # Create variable to determine if Breadth search is Used (Initialize to None)
    depth_search = None                                                         # Create variable to determine if Depth search is Used (Initialize to None)
    keyword_used = None                                                         # Create variable to determine if the optional keyword was included (Initialize to None)
    keyword = False                                                             # Create variable for the optional keyword string (Initializae to False)

    """
    ****************************************************************************
    * Description: initialize_state function
    ****************************************************************************
    """

    def initialize_state(self, arguments):
        self.num_args(arguments)                                                # Call the function to reference and store the number of arguments
        self.start_page(arguments[1])                                           # Call the function to reference and store the starting URL
        self.search_type(arguments[2])                                          # Call the function to reference and store the search type
        self.depth_limit(arguments[3])                                          # Call the function to reference and store the limit for the search depth
        if self.num_arguments == 5:                                             # If the number of the arguments is five then then the optional keyword was input
            self.set_keyword(arguments[4])                                      # Call the function to  reference and store the keyword elements

    """
    ****************************************************************************
    * Description: num_args function
    ****************************************************************************
    """

    def num_args(self, arguments):
        self.num_arguments = len(arguments)

    """
    ****************************************************************************
    * Description: start_page function
    ****************************************************************************
    """

    def start_page(self, url):
        self.starting_url = url

    """
    ****************************************************************************
    * Description: search_type function
    ****************************************************************************
    """

    def search_type(self, type):
        if type == "breadth":                                                   # If Search option Breadth-First was selected
            self.breadth_search = True                                          # Set the Breadth First Seatch to True
            self.depth_search = False                                           # Set the Depth First Search to False
        if type == "depth":                                                     # If Search option Depth-First was selected
            self.depth_search = True                                            # Set the Depth First Search to False
            self.breadth_search = False                                         # Set the Breadth First Seatch to True

    """
    ****************************************************************************
    * Description: depth_limit function
    ****************************************************************************
    """

    def depth_limit(self, dep_lim):
        self.depth = int(dep_lim)

    """
    ****************************************************************************
    * Description: set_keyword function
    * Function is used to set the class variables that indicate a keyword was
    * input for the search and store the keyword for later use
    ****************************************************************************
    """

    def set_keyword(self, key_word):
        self.keyword_used = True                                                # Return true indicating that the optional keyword exists
        self.keyword = key_word                                                 # Set the keyword to the user input string in the forth array element
