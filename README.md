# BINUS Locator Program  

Program made using GMplot and Python.  
It is used to draw a map containing nodes that lead to a specific place on earth based on the coordinates in coords23.csv, these locations have been handpicked by us and as you can see from the live preview it will try to find the shortest path to all of these places using either Johnson's or the Floyd Warshall algorithm.  
Documentation is located in the documentation folder in both pdf and docx forms.

Made by:
- Peter Nelson Subrata - 2502023562
- Philipus Adriel Tandra - 2502031715
- Christopher Owen - 2502019180
- Arvin Yuwono - 2502009721

Live Preview : https://pewterzz.github.io/BINUS-Locator/html/index.html

How to use Python Code:  

To use the main and mainFloyd files you need to locate the directory they are located in by doing the command below on the console.
```
cd BINUS-Locator
```  
Once you are in this directory you can run the main.py file for Johnson's algorithm or the mainFloyd.py file for the Floyd Warshall Algorithm version.  
Then you can choose whether or not you want to use an adjacency list or matrix and then from there you can choose what you want to see from a selection of options.
Since the data was inputted manually we chose to input our favourite places including restaurants, fun places (recreational), malls and other unviersities. The output will show the real distance to each of those places that we have inputted and it will also create or replace the html file in the algorithm folder.

If you have any other questions regarding the use of this program please contact me (Peter) via whatsapp.
