import snap
import random
from networkx import nx
from statistics import median
import math
import numpy as np

# function for initialize graph from a file
def create_graph(filePath):
    graph = snap.LoadEdgeList(snap.PNGraph, filePath, 0, 1)
    #print_info(graph)
    return graph

#function for the generation of a random graph
def random_graph_generator(nodes, edges, num):
    graph = nx.gnm_random_graph(nodes,edges)
    # print_info(graph)
    path = "Datasets/rnd_graph_"+num+".txt"
    fh = open(path, 'wb')
    nx.write_edgelist(graph, fh, encoding="utf-8")

#fuction for printing nodes info
def print_nodes_info(graph):
    for node in graph.Nodes():
        print_node_info(node)

#function for printing node info
def print_node_info(node):
    print("node: %d, out-degree %d, in-degree %d" % (node.GetId(), node.GetOutDeg(), node.GetInDeg()))

#function for printing information relating to the input graph
def print_info(graph):
    print("Number of nodes: ", graph.GetNodes())
    print("Number of edges: ", graph.GetEdges())
    print("Maximum degree: ", graph.GetNI(snap.GetMxDegNId(graph)).GetDeg())
    print("Diameter (approximate): ", snap.GetBfsFullDiam(graph, 10))
    print("Triangles: ", snap.GetTriads(graph))
    print("Clustering coefficient: ", snap.GetClustCf(graph))

#function to eliminate edges with randomly generated probabilities
def edge_random_probability(graph):
    print("Number of starting edges: ", graph.GetEdges())
    for n in graph.Nodes():
        for e in n.GetOutEdges():
            random_edge_probability = round(random.uniform(0.1, 1), 5)
            random_del_probability = round(random.uniform(0.1, 1), 5)
            if random_edge_probability >= random_del_probability:
                graph.DelEdge(n.GetId(), e)            
    print("Number of remaining edges: ", graph.GetEdges())

#function to eliminate edges with probability proportional to the degree of the node
def edge_proportional_to_degree_probability(graph):
    print("Number of starting edges: ", graph.GetEdges())
    for n in graph.Nodes():
        for e in n.GetOutEdges():
            random_edge_probability = (1/n.GetDeg())
            random_del_probability = random.random()
            if random_edge_probability >= random_del_probability:
                graph.DelEdge(n.GetId(), e)
    print("Number of remaining edges: ", graph.GetEdges())

#function to set random thresholds to the edges of the graph
def set_random_threshold(graph):
    g = snap.ConvertGraph(snap.PNEANet, graph) # PNEANet correspond to TNEANet, conversion of graph in directed multigraphs (multiple directed edges between an ordered pair of nodes) with attributes for nodes and edges
    for n in g.Nodes():
        #max= n.GetDeg() + int((n.GetDeg()/100)*20+1)
        random_value = random.randint(0, n.GetDeg())
        g.AddIntAttrDatN(n.GetId(), random_value, "threshold")
        #print("Threshold of the node ", n.GetId()," with value", g.GetIntAttrDatN(n.GetId(),"threshold"))
    return g

#function to set fixed thresholds to the edges of the graph
def set_fixed_threshold(graph, value):
    g = snap.ConvertGraph(snap.PNEANet, graph)
    for n in g.Nodes():
        g.AddIntAttrDatN(n.GetId(), value, "threshold")
    return g


#function to set thresholds based on the most frequent value
def set_most_frequent_threshold(graph):
    g = snap.ConvertGraph(snap.PNEANet, graph)
    data=[]
    # print("Number of graph nodes: ", g.GetNodes())
    count=0
    for n in g.Nodes():
        data.append(n.GetDeg())
    values = np.array(data)
    counts = np.bincount(values)
    value = np.argmax(counts)
    print("The most frequent value is: ", value)
    for n in g.Nodes():
        g.AddIntAttrDatN(n.GetId(), value, "threshold")
        # print("Threshold of the node ", n.GetId(), " with value ", g.GetIntAttrDatN(n.GetId(), "threshold"))
        if n.GetDeg()<value:
            count+=1
    print("Number of nodes below the most frequent value: ", count)
    return g

#function to set thresholds based on the value of the median
def set_median_threshold(graph):
    g = snap.ConvertGraph(snap.PNEANet, graph)
    data=[]
    # print("Number of graph nodes: ", g.GetNodes())
    count=0
    for n in g.Nodes():
        data.append(n.GetDeg())
    value = median(data)
    print("The median value is: ", value)
    for n in g.Nodes():
        g.AddIntAttrDatN(n.GetId(), value, "threshold")
        # print("Threshold of the node ", n.GetId(), " with value ", g.GetIntAttrDatN(n.GetId(), "threshold"))
        if n.GetDeg()<value:
            count+=1
    print("Number of nodes below the median: ", count)
    return g

#function to set proportional to degree thresholds to the edges of the graph
def set_degree_proportional_thresholds(graph, value):
    g = snap.ConvertGraph(snap.PNEANet, graph)
    # print("Number of graph nodes: ", g.GetNodes())
    for n in g.Nodes():
        g.AddIntAttrDatN(n.GetId(), math.floor(n.GetDeg() * value) + 1, "threshold")
    return g