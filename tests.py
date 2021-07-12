#import random
import copy
import numpy as np
from networkx.generators.degree_seq import DegreeSequenceRandomGraph
import test
import graph 
import ast
#graph.random_graph_generator(1000,10000,'2')
#g = graph.create_graph('Datasets/rnd_graph_2.txt')
#graph.print_info(g)
#test.proportional_mostfrequent_test('rnd_graph_2', 'Datasets/rnd_graph_2.txt')
'''def getNodesList() :
    f = open('Tests/deezer_tests/test_pmf.csv')
    f.readline()
    lines = f.readlines()
    l = []
    for line in lines :
        iteration = line.split('{')[0]
        results = line.split('{')[1]
        d = ast.literal_eval('{'+results)
        l.append(d)
        #print(len(d))
        #print(sum(d.values()))
    return l
'''
def sumValues() :
    avg_nodes = np.zeros(20)
    #print(avg_nodes)
    avg_incentives = np.zeros(20)
    f = open('Tests_old/rnd_graph_1_tests/test_rr.csv')
    f.readline()
    lines = f.readlines()
    for line in lines :
        iteration = line.split('{')[0].replace(" ", "")
        results = line.split('{')[1]
        d = ast.literal_eval('{'+results)
        #print(int(iteration) - 1, len(d))
        avg_nodes[int(iteration)  ] += sum([1 for i in d.values() if i != 0 ])
        avg_incentives[int(iteration) ] += sum(d.values())
    file_name = 'Tests/rnd_graph_1_tests/test_rr.csv'   
    open(file_name, 'a+').write("%s\n" % (avg_incentives))  
    open(file_name, 'a+').write("%s\n" % (avg_nodes)) 
    
    #print(avg_nodes)
    #print(avg_incentives)
        #print("Iterazione " +iteration)
        #print(sum(d.values()))
        #print(len(d))
'''
def edge_proportional_to_degree_probability(g):
    print("Number of starting edges: ", g.GetEdges())
    remove_edge = []
    OutDegV = g.GetNodeOutDegV() #[{id, deg},.,.,.,.,.,.,.,.,.]
    nodeList = {}
    for item in OutDegV:
        if(type(item.GetVal2()) == None) : print("node ID %d: out-degree %d" % (item.GetVal1(), item.GetVal2()))
        nodeList[item.GetVal1()] = item.GetVal2()
        #{id: deg,........}
    #print(nodeList)
    remove_edge = []
    for e in g.Edges():
        nodeId = e.GetSrcNId()
        deg = nodeList.get(nodeId);
        #print("node ID %d: in-degree %d" % (nodeId, deg))
        random_edge_probability = (1/int(deg))
        random_del_probability = 0.5
        if random_edge_probability >= random_del_probability:
            #print("%f %f" % (random_del_probability, random_edge_probability))
            remove_edge.append(e)
    print(len(remove_edge))
    print("Number of remaining edges: ", g.GetEdges() - len(remove_edge))

def edge_proportional_to_degree_probability2(graph, graph2):
    print("Number of starting edges: ", graph.GetEdges())
    degree = g.GetDegSeqV() #[{id, deg},.,.,.,.,.,.,.,.,.]
    nodeList = {}
    for i in range(0, degree.Len()):
        if(type(degree[i]) == None) : print("node ID %d: out-degree %d" % (item.GetVal1(), item.GetVal2()))
        nodeList[i] = degree[i]
    remove_edge = []
    remove_edge2 = []
    for n in graph.Nodes():
        for e in n.GetOutEdges():
            nodeId = n.GetId()
            deg = nodeList.get(nodeId);
            print(deg)
            #if deg != n.GetDeg() : print("grado calcolato con lista %d grado calcolato da nodo %d" % (deg, n.GetDeg()));
            #print("%f %f" % (1/int(deg),1/n.GetOutDeg()))
            #random_edge_probability = (1/int(deg))
            random_del_probability = random.random()
            if 1/deg != 1/n.GetOutDeg(): print("%f %f" % (deg, n.GetDeg()) )
            if 1/deg >= random_del_probability:
                #print("%f %f" % (random_del_probability, random_edge_probability))
                remove_edge.append(e)
            if 1/n.GetDeg() >= random_del_probability:
                remove_edge2.append(e)
        for dest in remove_edge:
            graph.DelEdge(n.GetId(), dest)
        for dest in remove_edge2:
            graph2.DelEdge(n.GetId(), dest)
    #print("%d %d" % (len(remove_edge), len(remove_edge2)))
    print("Number of remaining edges: ", graph.GetEdges())
    print("Number of remaining edges: ", graph2.GetEdges())

def edge_random_probability(graph):
    print("Number of starting edges: ", graph.GetEdges())
    remove_edge = []
    for e in graph.Edges():
        random_edge_probability = round(random.uniform(0.1, 1), 5)
        random_del_probability = round(random.uniform(0.1, 1), 5)
        if random_edge_probability >= random_del_probability:
            remove_edge.append(e)
        
    print("Number of remaining edges: ", graph.GetEdges() - len(remove_edge))

#g = graph.random_graph_generator(10000,45000,"1")
#graph.print_info(g)
#g2 = graph.create_graph('Datasets/deezer.txt')
#edge_proportional_to_degree_probability(g)
#edge_proportional_to_degree_probability2(g, g2)'''
sumValues()
#test.random_random_test('bitcoin','Datasets/bitcoin.txt')