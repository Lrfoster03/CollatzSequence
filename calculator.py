import networkx as nx
import matplotlib.pyplot as plt

sequence = []
G = nx.DiGraph()

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
    for i in range(len(sequence) - 1):
        G.add_edge(str(sequence[i]), str(sequence[i+1]))

    # Add error handling in the event that the user enters a number that is less than 4 (aka 2 or 1)

    values = [val_map.get(node, 0.75) for node in G.nodes()]
    # Specify the edges you want here
    red_edges = [("4", "2"), ("2", "1"), ("1", "4")]
    edge_colours = ['black' if not edge in red_edges else 'red'
                    for edge in G.edges()]
    black_edges = [edge for edge in G.edges()]
    # Need to create a layout when doing
    # separate calls to draw nodes and edges
    pos = nx.spring_layout(G)
    nx.draw_networkx_nodes(G, pos, cmap=plt.get_cmap('jet'), 
                        node_color = values, node_size = 500)
    nx.draw_networkx_labels(G, pos)
    nx.draw_networkx_edges(G, pos, edgelist=red_edges, edge_color='r', arrows=True)
    nx.draw_networkx_edges(G, pos, edgelist=black_edges, arrows=False)
    plt.show()

# These edges will always exist in a collatz sequence (As 1-> 4 -> 2 -> 1 is a cycle)
G.add_edges_from([("1", "4"), ("4", "2"), ("2", "1")])
val_map = {"1": 1.0,
        "2": 0.6,
        "4": 0.8}


response = input("Enter a number, or type exit() to quit: ")
while True:
    if(response == "exit()"):
        break
    elif(type(response) is str and response.isdigit()):
        response = int(response)
        if(response > 0):
            sequence = []
            computeSequence(response)
            print("Completed in " + str(len(sequence)) + " iterations.")
            print(sequence)
            plotSequence()
        else:
            print("Invalid input")
    else:
        # print("Invalid input")

        response = input("Enter another number, or type exit() to quit: ")
