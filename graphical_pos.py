import networkx as nx

def graphical_pos(G, width=1., vert_gap = 0.2, vert_loc = 0, xcenter = 0.5):
    """
    Creates a tree based representation of a graph from the bottom up specifically for the Collatz Conjecture, starting at node 4.
    
    Example: 
                              5   32
                               \\  /  
                                16
                                 |
                                 8
                                 | 
                                 4
                                / \\
                               2 - 1
    G: the graph
    
    width: horizontal space allocated for this branch - avoids overlap with other branches
    
    vert_gap: gap between levels of hierarchy
    
    vert_loc: vertical location of root
    
    xcenter: horizontal location of root
    """

    # Root is always set to the graph value of 4
    root = 4

    def _graphical_pos(G, root, width=1., vert_gap = 0.2, vert_loc = 0, xcenter = 0.5, pos = None, parent = None):
        '''

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
                pos = _graphical_pos(G,child, width = dx, vert_gap = vert_gap, 
                                    vert_loc = vert_loc-vert_gap, xcenter=nextx,
                                    pos=pos, parent = root)
        return pos
    return _graphical_pos(G, root, width, vert_gap, vert_loc, xcenter)