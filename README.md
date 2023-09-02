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
