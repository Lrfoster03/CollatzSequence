# CollatzSequence

This is a a Collatz sequence calculator designed to compute a Collatz sequence, and then display as a directed graph. 

This calculator also accepts multiple inputs and shows how the different sequences converge to 1. 

Its built using Python 3.11, NetworkX, and MatPlotLib. For starters, ensure that you have the latest install of Python 

Then in a terminal run ```pip install networkx``` and ```pip install matplotlib```

When running the application, you should be given a prompt to enter a number. This only works for integers greater than 0. There is error handling built into the application, but it is most likely still possible to crash.

Upon entering a number, you will see in the terminal a display of the sequence until it reaches 1, and a pop-up of the directed graph that is produced. Upon exiting the pop-up, you will then be prompted to enter another number. 

At any time you can exit the application by typing ```exit()```

Heres an example of how a directed graph would look using the inputs 234 and 35. 

