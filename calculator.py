import networkx as nx
import matplotlib.pyplot as plt

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
    G.add_edges_from([(1, 4), (4, 2), (2, 1)])

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
    pos = nx.spiral_layout(G, scale = 10, equidistant = True)
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
