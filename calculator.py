import networkx as nx
import matplotlib.pyplot as plt
from networkx.drawing.nx_agraph import graphviz_layout
import pygraphviz

sequence = []
G = nx.DiGraph()
color_map = []
red_edges = [(4, 2), (2, 1), (1, 4)]
inputs = []

def computeSequence(input):
    # Clear the sequence before computing a new one
    sequence.append(input.__int__())
    if input == 1:
        return 
    elif input % 2 == 0:
        return computeSequence(input / 2)
    else:
        return computeSequence(3 * input + 1)
    
def plotSequence():
    node = 0
    # Highlight converged points
    for x in sequence:
        if (G.has_node(x)):
            # If the node is an input, highlight it as a different color
            if x in inputs:
                val_map[x] = 0.7
            else:
                val_map[x] = 0.8
            break

    for i in range(len(sequence) - 1): 
        G.add_edge((sequence[i]), (sequence[i+1]))   

    # These edges will always exist in a collatz sequence (As 1-> 4 -> 2 -> 1 is a cycle)
    # G.add_edges_from([(1, 4), (4, 2), (2, 1)])

    # Highlight starting points
    val_map[response] = 0.5

    values = [val_map.get(node, 0.72) for node in G.nodes()]
    
    # Specify the edges you want here

    values[0] = 1
    edge_colours = ['black' if not edge in red_edges else 'red'
                    for edge in G.edges()]
    black_edges = [edge for edge in G.edges()]
    # Need to create a layout when doing
    # separate calls to draw nodes and edges
    # pos = nx.spring_layout(G, k=0.15, iterations=20)
    
    # pos = nx.shell_layout(G, scale=5)
    pos = graphviz_layout(G, prog="neato")
    # pos = hierarchy_pos(G, 1)
    # pos = nx.spiral_layout(G, scale = 10, equidistant = True)
    nx.draw_networkx_nodes(G, pos, cmap=plt.get_cmap('jet'), 
                        node_color = values, node_size = 500)
    nx.draw_networkx_labels(G, pos)
    nx.draw_networkx_edges(G, pos, edgelist=red_edges, edge_color='r', arrows=True)
    nx.draw_networkx_edges(G, pos, edgelist=black_edges, arrows=False)
    nx.draw_networkx_edge_labels(
    G, pos,
    edge_labels={('A', 'B'): 'AB', 
                 ('B', 'C'): 'BC', 
                 ('B', 'D'): 'BD'},
    font_color='red'
    )
    # print(values)
    plt.show()

def hierarchy_pos(G, root=None, width=1., vert_gap = 0.2, vert_loc = 0, xcenter = 0.5):

    '''
    From Joel's answer at https://stackoverflow.com/a/29597209/2966723.  
    Licensed under Creative Commons Attribution-Share Alike 
    
    If the graph is a tree this will return the positions to plot this in a 
    hierarchical layout.
    
    G: the graph (must be a tree)
    
    root: the root node of current branch 
    - if the tree is directed and this is not given, 
      the root will be found and used
    - if the tree is directed and this is given, then 
      the positions will be just for the descendants of this node.
    - if the tree is undirected and not given, 
      then a random choice will be used.
    
    width: horizontal space allocated for this branch - avoids overlap with other branches
    
    vert_gap: gap between levels of hierarchy
    
    vert_loc: vertical location of root
    
    xcenter: horizontal location of root
    '''
    if not nx.is_tree(G):
        raise TypeError('cannot use hierarchy_pos on a graph that is not a tree')

    if root is None:
        if isinstance(G, nx.DiGraph):
            root = next(iter(nx.topological_sort(G)))  #allows back compatibility with nx version 1.11
        else:
            root = random.choice(list(G.nodes))

    def _hierarchy_pos(G, root, width=1., vert_gap = 0.2, vert_loc = 0, xcenter = 0.5, pos = None, parent = None):
        '''
        see hierarchy_pos docstring for most arguments

        pos: a dict saying where all nodes go if they have been assigned
        parent: parent of this branch. - only affects it if non-directed

        '''
    
        if pos is None:
            pos = {root:(xcenter,vert_loc)}
        else:
            pos[root] = (xcenter, vert_loc)
        children = list(G.neighbors(root))
        if not isinstance(G, nx.DiGraph) and parent is not None:
            children.remove(parent)  
        if len(children)!=0:
            dx = width/len(children) 
            nextx = xcenter - width/2 - dx/2
            for child in children:
                nextx += dx
                pos = _hierarchy_pos(G,child, width = dx, vert_gap = vert_gap, 
                                    vert_loc = vert_loc-vert_gap, xcenter=nextx,
                                    pos=pos, parent = root)
        return pos
    return _hierarchy_pos(G, root, width, vert_gap, vert_loc, xcenter)


val_map = {1: 0.9,
        2: 0.6,
        4: 0.8}


response = input("Enter a number, or type exit to quit: ")
while True:
    if(response == "exit()" or response == "exit" or response == "quit" or response == "q" or response == "e"):
        break
    elif(type(response) is str and response.isdigit()):
        response = int(response)
        if(response > 0):
            inputs.append(response)
            sequence = []
            computeSequence(response)
            print("Completed in " + str(len(sequence)) + " iterations.")
            print(sequence)
            plotSequence()
        else:
            print("Invalid input. Please enter a positive integer.")
    else:
        # print("Invalid input")

        response = input("Enter another number, or type exit to quit: ")


