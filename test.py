from random import random
from tpi import tpi
import graph
import numpy as np

# RANDOM PROBABILITY - FIXED THRESHOLD
def random_fixed_test(dataset, path):
    avg = np.zeros(10)
    file_name = "Tests/"+dataset+"_tests/test_rf.csv"
    open(file_name, 'w+').write("Threshold AVG_Incentives\n")
    iterations = 50

    for j in range(0, iterations):
        g = graph.create_graph(path)
        graph.edge_random_probability(g)
        for i in range(0, 10):
            g = graph.set_fixed_threshold(g, i+1)
            tot_incentives = tpi.tpi(g)
            avg[i] += tot_incentives

    for y in range(0, 10):
        open(file_name, 'a+').write("%d %d\n" % (y+1, avg[y]/iterations))

# RANDOM PROBABILITY - RANDOM THRESHOLD
def random_random_test(dataset, path):
    avg = 0
    file_name = "Tests/"+dataset+"_tests/test_rr.csv"
    open(file_name, 'w+').write("Iteration Incentives\n")
    iterations = 50

    for j in range(0, iterations):
        g = graph.create_graph(path)
        graph.edge_random_probability(g)
        g = graph.set_random_threshold(g)
        tot_incentives = tpi.tpi(g)
        avg += tot_incentives
        open(file_name, 'a+').write("%d %d\n" % (j+1, tot_incentives))

    open(file_name, 'a+').write("Media %d\n" % (avg/iterations))

# RANDOM PROBABILITY - PROPORTIONAL TO DEGREE THRESHOLD
def random_proportional_test(dataset, path):
    avg = np.zeros(10)
    file_name = "Tests/"+dataset+"_tests/test_rp.csv"
    open(file_name, 'w+').write("Threshold AVG_Incentives\n")
    iterations = 50

    for j in range(0, iterations):
        g = graph.create_graph(path)
        graph.edge_random_probability(g)
        for i in range(0, 10):
            g = graph.set_degree_proportional_thresholds(g, (i+1)/10)
            tot_incentives = tpi.tpi(g)
            avg[i] += tot_incentives

    for y in range(0, 10):
        open(file_name, 'a+').write("%d %d\n" % (y+1, avg[y]/iterations))

# RANDOM TO DEGREE PROBABILITY - MEDIAN THRESHOLD
def random_median_test(dataset, path):
    avg = np.zeros(10)
    file_name = "Tests/"+dataset+"_tests/test_rm.csv"
    open(file_name, 'w+').write("Threshold AVG_Incentives\n")
    iterations = 50

    for j in range(0, iterations):
        g = graph.create_graph(path)
        graph.edge_random_probability(g)
        for i in range(0, 10):
            g = graph.set_median_threshold(g)
            tot_incentives = tpi.tpi(g)
            avg[i] += tot_incentives

    for y in range(0, 10):
        open(file_name, 'a+').write("%d %d\n" % (y+1, avg[y]/iterations))

# RANDOM TO DEGREE PROBABILITY - MOST FREQUENT THRESHOLD
def random_mostfrequent_test(dataset, path):
    avg = np.zeros(10)
    file_name = "Tests/"+dataset+"_tests/test_rmf.csv"
    open(file_name, 'w+').write("Threshold AVG_Incentives\n")
    iterations = 50

    for j in range(0, iterations):
        g = graph.create_graph(path)
        graph.edge_random_probability(g)
        for i in range(0, 10):
            g = graph.set_most_frequent_threshold(g)
            tot_incentives = tpi.tpi(g)
            avg[i] += tot_incentives

    for y in range(0, 10):
        open(file_name, 'a+').write("%d %d\n" % (y+1, avg[y]/iterations))

# PROPORTIONAL TO DEGREE PROBABILITY - PROPORTIONAL TO DEGREE THRESHOLD
def proportional_proportional_test(dataset, path):
    avg = np.zeros(10)
    file_name = "Tests/"+dataset+"_tests/test_pp.csv"
    open(file_name, 'w+').write("Threshold AVG_Incentives\n")
    iterations = 50

    for j in range(0, iterations):
        g = graph.create_graph(path)
        graph.edge_proportional_to_degree_probability(g)
        for i in range(0, 10):
            g = graph.set_degree_proportional_thresholds(g, (i + 1) / 10)
            tot_incentives = tpi.tpi(g)
            avg[i] += tot_incentives

    for y in range(0, 10):
        open(file_name, 'a+').write("%d %d\n" % (y + 1, avg[y] / iterations))

# PROPORTIONAL TO DEGREE PROBABILITY - FIXED THRESHOLD
def proportional_fixed_test(dataset, path):
    avg = np.zeros(10)
    file_name = "Tests/"+dataset+"_tests/test_pf.csv"
    open(file_name, 'w+').write("Threshold AVG_Incentives\n")
    iterations = 50

    for j in range(0, iterations):
        g = graph.create_graph(path)
        graph.edge_proportional_to_degree_probability(g)
        for i in range(0, 10):
            g = graph.set_fixed_threshold(g, i+1)
            tot_incentives = tpi.tpi(g)
            avg[i] += tot_incentives

    for y in range(0, 10):
        open(file_name, 'a+').write("%d %d\n" % (y+1, avg[y]/iterations))
        
# PROPORTIONAL TO DEGREE PROBABILITY - RANDOM THRESHOLD
def proportional_random_test(dataset, path):
    avg = np.zeros(10)
    file_name = "Tests/"+dataset+"_tests/test_pr.csv"
    open(file_name, 'w+').write("Threshold AVG_Incentives\n")
    iterations = 50

    for j in range(0, iterations):
        g = graph.create_graph(path)
        graph.edge_proportional_to_degree_probability(g)
        for i in range(0, 10):
            g = graph.set_random_threshold(g)
            tot_incentives = tpi.tpi(g)
            avg[i] += tot_incentives

    for y in range(0, 10):
        open(file_name, 'a+').write("%d %d\n" % (y+1, avg[y]/iterations))

# PROPORTIONAL TO DEGREE PROBABILITY - MEDIAN THRESHOLD
def proportional_median_test(dataset, path):
    avg = np.zeros(10)
    file_name = "Tests/"+dataset+"_tests/test_pm.csv"
    open(file_name, 'w+').write("Threshold AVG_Incentives\n")
    iterations = 50

    for j in range(0, iterations):
        g = graph.create_graph(path)
        graph.edge_proportional_to_degree_probability(g)
        for i in range(0, 10):
            g = graph.set_median_threshold(g)
            tot_incentives = tpi.tpi(g)
            avg[i] += tot_incentives

    for y in range(0, 10):
        open(file_name, 'a+').write("%d %d\n" % (y+1, avg[y]/iterations))

# PROPORTIONAL TO DEGREE PROBABILITY - MOST FREQUENT THRESHOLD
def proportional_mostfrequent_test(dataset, path):
    avg = np.zeros(10)
    file_name = "Tests/"+dataset+"_tests/test_pmf.csv"
    open(file_name, 'w+').write("Threshold AVG_Incentives\n")
    iterations = 50

    for j in range(0, iterations):
        g = graph.create_graph(path)
        graph.edge_proportional_to_degree_probability(g)
        for i in range(0, 10):
            g = graph.set_most_frequent_threshold(g)
            tot_incentives = tpi.tpi(g)
            avg[i] += tot_incentives

    for y in range(0, 10):
        open(file_name, 'a+').write("%d %d\n" % (y+1, avg[y]/iterations))

g = graph.create_graph('Datasets/rnd_graph_1.txt')
graph.print_info(g)
#random_fixed_test('rnd_graph_1','Datasets/rnd_graph_1.txt')