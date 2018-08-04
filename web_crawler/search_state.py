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
**
** Example Form Return:
** {'starting_url': 'https://www.google.com', 'method': 'value', 'depth': 12, 'keyword': 'find me'}
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
    depth = None                                                                # Create variable for the search limit depth (Initialize to N)
    keyword_used = None                                                         # Create variable to determine if the optional keyword was included (Initialize to None)
    keyword = False                                                             # Create variable for the optional keyword string (Initializae to False)

    """
    ****************************************************************************
    * Description: initialize_state function
    ****************************************************************************
    """

    def initialize_state(self, form_data):
        self.num_args(len(form_data))                                           # Call the function to reference and store the number of arguments
        self.search_type(form_data['method'])                                   # Call the function to reference and store the search type
        self.start_page(form_data['starting_url'])                              # Call the function to reference and store the starting URL
        self.depth_limit(form_data['depth'])                                    # Call the function to reference and store the limit for the search depth
        if form_data['keyword']:                                                # If the number of the arguments is five then then the optional keyword was input
            self.set_keyword(form_data['keyword'])                              # Call the function to  reference and store the keyword elements

    """
    ****************************************************************************
    * Description: num_args function
    ****************************************************************************
    """

    def num_args(self, arguments):
        self.num_arguments = arguments

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
            self.breadth_search = False                                         # Set the Breadth First Search to True

    """
    ****************************************************************************
    * Description: depth_limit function
    ****************************************************************************
    """

    def depth_limit(self, dep_lim):
        if int(dep_lim) < 1:
            self.depth = 1
        elif self.breadth_search and int(dep_lim) > 3:
            self.depth = 3
        elif self.depth_search and int(dep_lim) > 100:
            self.depth = 100
        else:
            self.depth = int(dep_lim)                                           # Set the search to the limit from the form (as an integer)

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
