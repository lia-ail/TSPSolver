# TSPSolver

TSPSolver is desktop application for solving Travelling Salesman Problem. It uses Python programming language, including such libraries as: pandas, tkinter, pillow, CustomTkinter.

The travelling salesman problem (TSP) asks the following question: 
"Given a list of cities and the distances between each pair of cities, what is the shortest possible route that visits each city exactly once and returns to the origin city?"
It is an NP-hard problem in combinatorial optimization, important in theoretical computer science and operations research.

In TSPSolver, as main algorithms I used dynamic programming(DP) algorithm and nearest neighbor(NN) algorithm. The reason why I used two algorithms is mentioned above:
The travelling salesman problem is an NP-hard problem. This means that there is no such an algorithm, that will provide precise results in time other than exponential.
So, in my case, DP algorithm will provide accurate results with efficient time only for small data sets. For medium and large data sets user can swap algorithm to the NN algorithm.
Anyway, possibility of trying to get precise results from such data sets using DP algorithm remains.
Although NN algorithm is not as accurate as the DP algorithm, it is still capable of producing good approximate results and is very efficient in terms of time complexity.

In DP algorithm i used helper recursive function, bitmask and memoization table. Memoization table will be size of n*2^n where n is a number of cities and will help us to save results of in-between calculations.
Bitmask is an efficient way of keeping track of visited cities. Helper recursive function first will compute first optimal result and then will compare different routes and results with current optimal result to
decide, Should It Stay or Should It Go (stick with old optimal result or take a new route.)

On the other hand, NN algorithm is pretty much simple greedy approach. For each city, picks the most minimum/maximum value from the remaining cities.

The project files consist of 5 files and are located in the "dsd" folder: "praktiks.py", "dynamic_example.py", "nearest_neighbor.py", "calculator.py" and "vector-calculator-icon.jpg" respectively.
In this project, I followed a modular project structure, so I divided the four parts of the program, which can be reused in different projects in the future, into four modules:
"praktiks.py" is the main project file (it should be named "main") and to this module is imported all of the remaining modules. Basically it is realisation of the UI and connection between UI and algorithms;
"dynamic_example.py" and "nearest_neighbor.py" are basically realisations of the DP and NN algorithms;
"calculator.py" - a module with the implementation of a calculator that uses the reversed polish notation algorithm under the hood. In case user will need to recalculate something in-place, there will be my calculator.

"vector-calculator-icon.jpg" is just icon for the calculator button.

Once user opens application (executes "praktiks.py"), main window appears: ![Screenshot_1](https://github.com/lia-ail/TSPSolver/assets/120140396/386c25ae-b99e-42f9-8225-a7122c2ec41c)

There user can see "Calculator" button at top left corner. This button calls module "calculator.py". Calculator looks the following way: ![Screenshot_2](https://github.com/lia-ail/TSPSolver/assets/120140396/b658630c-105c-461c-89f0-2c80908f6fa9)

At top right corner user can see a menu, that allows to decide, which algorithm will be used to solve the problem: ![Screenshot_3](https://github.com/lia-ail/TSPSolver/assets/120140396/31207c56-2317-44d6-a612-ae3b12d13de8)

Then at the top middle part of the window, user can see text area, which will serve as display area to display user input and outout route.
Lower user can see two menus. Left menu allows to choose, in which mode the program will perform: maximum or minimum.
Right menu allows to choose, in which currency expenses/income will be displayed.

And finally, user can see four buttons at the bottom of the window. They are "Create table", "Open a File", "Solve", "Save".
"Create table" button invokes a command which opens new window: 
![Screenshot_4](https://github.com/lia-ail/TSPSolver/assets/120140396/a30667c9-a35a-4c50-8350-d5a8b932d3e2)

There user will find input field, "Clear", "Create table", "Done" buttons.
Input field takes a number x (x <= 5) as input and once "Create table" button is clicked, creates an input matrix with size of x*x:
![Screenshot_5](https://github.com/lia-ail/TSPSolver/assets/120140396/cd00689f-5ef1-4ee5-8da0-9466b6b0eede)

"Clear" button will delete input table, if exists.
"Done" button is capable of finishing with manual input. If input table does not exist, it will ask user if he wants to close "Create table" window. 
Else, it will check if there are not non-empty cells and input values are valid. If it is True, then it will read all of the values, create new matrix and pass it to the main window. Else, warning message will accure.

Next button from the main window is "Open a File". It will open file dialogue, proposing user to choose frome .xlsx or .csv files.
For correct work of the program, format of the matrices is expected to be as one of the following:
1. Without any pre-defined names:
   
   if .xlsx                            
   
   0 10 15 20                          
                    
   10 0 25 30                          
   
   15 25 0 35                          
   
   20 30 35 0                          

   if .csv

   0, 10, 15, 20

   10, 0, 25, 30

   15, 25, 0, 35

   20, 30, 35, 0
   
3. With pre-defined names for columns:
   
   if .xlsx                 
   
   A  B  C  D               
   
   0 10 15 20            
   
   10 0 25 30               
   
   15 25 0 35               
   
   20 30 35 0               

   if .csv

   A, B, C, D

   0, 10, 15, 20

   10, 0, 25, 30

   15, 25, 0, 35

   20, 30, 35, 0
   
5. With pre-defined names for both rows and columns:
    if .xlsx
                    
     A  B  C  D               
   
  A  0 10 15 20              
  
  B  10 0 25 30              
  
  C  15 25 0 35              
  
  D  20 30 35 0              

  , A, B, C, D

  A, 0, 10, 15, 20

  B, 10, 0, 25, 30

  C, 15, 25, 0, 35

  D, 20, 30, 35, 0

If file contains correct values, display area of the main window will look following way (manual input will look like that too):

![Screenshot_6](https://github.com/lia-ail/TSPSolver/assets/120140396/c4810ae2-04df-4161-9ef8-88a8cb83f36e)

"Solve" button solves travelling salesman problem for a given matrix and displays the resulting route and result:

![Screenshot_7](https://github.com/lia-ail/TSPSolver/assets/120140396/348dabef-b7e6-43bb-bff4-d3e39c2925a2)

"Save" button saves resulting route to the user-defined text file.

