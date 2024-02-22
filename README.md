# CollatzSequence

This is a a Collatz sequence calculator designed to compute a Collatz sequence, and then display as a directed graph. 

The Collatz conjecture is one of the most famous unsolved problems in mathematics. It can be described as follows:

![Example Collatz Sequence](media/CollatzPeacewise.png)

Where n is any natural number (Integer greater than 0).

This calculator also accepts multiple inputs and shows how the different sequences converge to 1. 

Its built using Python 3.11, NetworkX, and MatPlotLib. For starters, ensure that you have the latest install of Python 

Then in a terminal run ```pip install networkx``` and ```pip install matplotlib```

When running the application, you should be given a prompt to enter a number. This only works for integers greater than 0. There is error handling built into the application, but it is most likely still possible to crash.

Upon entering a number, you will see in the terminal a display of the sequence until it reaches 1, and a pop-up of the directed graph that is produced. Upon exiting the pop-up, you will then be prompted to enter another number. 

At any time you can exit the application by typing ```exit()```

Here's an example of how a directed graph would look using the inputs 234 and 35. 

![Example Collatz Sequence](media/Example.png)

I built this because my professor mentioned one day how when he has trouble sleeping, he'll take whatever time it is, and perform the Collatz conjecture on it (I know, crazy right). I looked it up and then saw a bunch of different diagrams showing how different sequences would converge to 1, and I immediately thought how cool it would be to make a script that automatically did it. 

This isn't flawless however. Every time we render a new directed graph, the points are thrown out randomly across the surface. This is something I'm looking into fixing for the future. 

All in all, I'm pretty happy how this came out. If anyone does use this code then I'll consider this project a success!
