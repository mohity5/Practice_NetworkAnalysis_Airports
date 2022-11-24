import pandas as pd
import numpy as np
import networkx as nx


def NodeExtracter(Path):
    nodes_p = []

    for i in Path:
            if (type(i) == list):
                for j in i:
                    nodes_p = np.append(nodes_p,j)
            else:
                nodes_p = np.append(nodes_p,i)

    return nodes_p

def PathEdges(Path):
    edges = pd.DataFrame()
    pos = 0
    for i in Path:
        if (type(i) == list):
            for k in range(0,len(i)-1,1):
                edges[pos] = [i[k],i[k+1]]
                pos = pos + 1

        else:
            edges[pos] = [i[0],i[1]]
            
    edges = edges.transpose()
    return edges

def AddLocations(PathGraph, Airport_Loc):
    PathGraph.code = {}
    PathGraph.pos = {}

    for j in range(0,len(PathGraph.nodes()),1):
       node = np.array(PathGraph.nodes())[j]
       
       for k in range(0,Airport_Loc.shape[0],1):
          if(Airport_Loc['id'][k] == node):
            PathGraph.code[node] = Airport_Loc['code'][k]
            PathGraph.pos[node] = (float(Airport_Loc['lon'][k]), float(Airport_Loc['lat'][k]))

    return PathGraph

def CreateGraph(Path, Airport_Loc):
    
    PathGraph = nx.DiGraph()

    nodes = NodeExtracter(Path)
    edges = PathEdges(Path)

    for i in nodes:
        PathGraph.add_node(i)
    
    for j in range(0, edges.shape[0],1):
       PathGraph.add_edge(edges[0][j],edges[1][j])

    PathGraph = AddLocations(PathGraph, Airport_Loc)

    return PathGraph


