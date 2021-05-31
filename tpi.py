import snap
import graph

s_v = {}         # partial incentive initially assigned to v
d_v = {}         # nodes' degrees
k_v = {}         # nodes' thresholds
N_v = {}         # nodes' neighbours
nodes_list = []  # U

# Algorithm TPI
def tpi(graph):

    remaining_nodes = 0  # number of nodes remaining after algorithm runs
    nodes_with_incentives = 0  # number of nodes with incentives
    sum_s_v = 0  # sum of total incentives

    # initialization of nodes list
    initialize_nodelist(graph)

    # initialization of algorithm variables
    initialize_variables(graph)

    # Update of incentives

    # For loop on nodes_list
    for v in nodes_list:
        # The cycle stops when the list becomes empty.
        if not nodes_list:
            break
        # Case 1 
        # If the threshold is greater than the degree of the node, we update the value of the incentive (s_v) and the threshold (k_v)
        if k_v.get(v) > d_v.get(v): 
            s_v[v] = update_incentive(v)
            sum_s_v += s_v[v]
            nodes_with_incentives += 1
            k_v[v] = d_v[v]

            # If the threshold is 0, we eliminate the node from the nodes list.
            if k_v[v] == 0:
                nodes_list.remove(v)

        # Case 2
        # If the threshold is less than the degree, we choose a node to eliminate from the graph among all nodes
        else: 
            remaining_nodes += 1
            local_max = {}
            # for all nodes we compute the formula to calculate the local max
            for u in nodes_list:
                if d_v[u] != 0:
                    local_max[u] = calculate_localMax(u)

            # get node with max criteria
            node = max(local_max, key=local_max.get)

            # eliminate from all neighbours the node to remove from graph and we remove the node from graph
            eliminate_node(node)

    print("Number of total incentives: ", nodes_with_incentives, " with total value of ", sum_s_v, " and number of remaining nodes: ", remaining_nodes)
    return s_v

  # This function initializes the nodelist
def initialize_nodelist(graph):
    for n in graph.Nodes():
        nodes_list.append(n.GetId())

 # This function initializes variables
def initialize_variables(graph):
    for v in graph.Nodes():
        s_v[v.GetId()] = 0
        d_v[v.GetId()] = v.GetOutDeg()
        k_v[v.GetId()] = graph.GetIntAttrDatN(v.GetId(), "threshold")
        temp_neigh = []
        for Id in v.GetOutEdges():  # calculation of nodes' neighbours
            temp_neigh.append(Id)
        N_v[v.GetId()] = temp_neigh

# This function calculates the local max of nodes
def calculate_localMax(u):
    return (k_v[u] * (k_v[u] + 1)) / (d_v[u] * (d_v[u] + 1))

  # This function updates incentives of a node
def update_incentive(v):
    return (s_v[v] + k_v[v] - d_v[v])

# This function eliminates node
def eliminate_node(node):
    if N_v[node] is not None:
        for u in N_v[node]:
            d_v[u] -= 1
            if N_v[u] is not None:
                N_v[u] = N_v[u].remove(node)
        nodes_list.remove(node)