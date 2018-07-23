# CS467_Lyra_Web2
CS 467 Online Capstone Project  
Oregon State University (Summer 2018)  
Lyra Group Project  
WEB2: GRAPHICAL CRAWLER  

Group Members  
- Evin Colignon
- James Hippler
- Victor Wang

WEB2: GRAPHICAL CRAWLER: Write a web page that crawls the web, following links from place to place, building a graphical model of places traveled. Project code: "WEB2".

In this project, you'll be creating both a web site and *nix-based program that crawls the web starting at a particular home page, and maps out all links graphically for the user.

The artistic presentation of the graphics are up to you, but the final project must satisfy the following requirements:

- At your site, the user will enter a starting web page, indicate depth-first or breadth-first traversal, and specify a numeric limit that stops the crawl from continuing indefinitely.
- The user input will be transmitted to a program running on a server somewhere.
- The program will begin to follow the links of that starting web page, creating a log of where it visits.
- In a depth-first crawl, the program will start at the start page, randomly choose one of the links on that page, then follow it to the next page. Then, at the next page, it randomly chooses a link from the options available, and follows it. This makes a chain from the starting page. This continues until the program hits the page limit indicated.
- In a breadth-first crawl, the program will follow ALL links from the start page, and ALL links from each page it visits, until the crawler has reached the limit of pages deep (as measured from the start page) it should visit. Since this is likely to return a huge, sprawling graph, consider limiting the user's input with this kind of search to a small number. For example, a limit of 1 means display all pages linked from start page. Limit 2 means display all pages linked from limit 1 pages, and display all limit 1 pages.
- The results will be transmitted back to the web page for graphical display and a small amount of manipulation (perhaps zooming, or displaying and/or hiding labels). Results displayed should include the title and URL of each page, perhaps controlled in such a way as to appear only when the user hovers over them to conserve space (this is up to you). The user must be able to click on one of these page nodes which should open up that page in a new tab or window. You must display the nodes graphically: do not use only text. Graph nodes and lines should not overlap.
- As an option, the user should be able to type in a keyword that will halt the program from searching when it is discovered on a page (this page and keyword are not being searched for, they are merely being encountered by chance). This page must be highlighted in the graphical results shown to the user.
- The web page should store past starting pages (with possible associated keywords) in a cookie on the users computer that can be displayed, and restarted.

Tools and Technology Requirements:

- Your project MUST be hosted somewhere for me to test for grading purposes, though you will be required to submit source code.
- Do not use Javascript-style "alert()" pop-up boxes to relate information to the player. Your user interface should display all information without resorting to asking the web browser to pop-up a dialog.
- Do not use Adobe's Flash player or any other encapsulated app.
- Do not use Django or any form of Content Management System (CMS) to build the pages or site for you.
- You may use Node.js, bootstrap, React, Angular, and/or jQuery, etc. if you like.

Recommended Division of Labor:

1. Crawler Developer: writes the software that will crawl the world wide web, recording what it finds.
2. Data Transfer Developer: creates the format of the log files written by the crawler, and writes the handling of transmitting the data back and forth from the web page to the crawler. Perhaps also programs the encapsulating website hosting the UI.
3. Data Visualizer: Writes the HTML and Javascript required for gathering the user input and displaying the results.

Note: This project type is likely to graded by a TA.
