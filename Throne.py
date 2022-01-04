import csv
import random
import networkx as nx
import matplotlib.pyplot as plt
import scipy.special
from networkx import gnm_random_graph, erdos_renyi_graph, shortest_path_length, barabasi_albert_graph, gnp_random_graph
import collections


original = nx.Graph() #our graph
myDict = {} #dict: {key = video_id : val = list of tags}

with open('try.csv', encoding = 'cp850') as inp: #read file cp850
    csv_reader = csv.reader(inp)
    for rows in csv_reader:
        myDict[rows[0]] = list(rows[1].split('|'))
        original.add_node(rows[0])

for videoID1 in myDict:
    for videoID2 in myDict:
        if videoID1 != videoID2:
            for tag in myDict[videoID1][0]:
                if tag in myDict[videoID2][0]:
                    original.add_edge(videoID1, videoID2, label=tag)


# Data = open('stormofswords.csv', "r")
# next(Data, None)  # skip the first line in the input file
# GraphType = nx.Graph()
# original = nx.parse_edgelist(Data, delimiter=',', create_using=GraphType, nodetype=str, data=(('weight', float),))

original_nodes = list(original.nodes)
original_edges = list(original.edges)
# print("number of nodes original_nodes", len(original_nodes))
# print("number of edges original_nodes", len(original_edges))

# pos = nx.spring_layout(original)
# nx.draw(original, pos, node_color='purple', with_labels=False, node_size=30)
# plt.show()

# erdos graph = G(n,p)
erdos = erdos_renyi_graph(len(original_nodes), 0.00068, seed=None, directed=False)
# pos = nx.spring_layout(erdos)
# nx.draw(erdos, pos, with_labels=False,  node_size=30, node_color='blue')
# plt.show()
# print("number of edges erdos:", len(erdos.edges))
# print("number of nodes erdos: ", erdos.number_of_nodes())
# gnp = nx.Graph()
# nx.draw(gnp_random_graph(len(original_nodes), 0.07, seed=None, directed=False), node_size=10, node_color='blue')
# plt.show()

# Gibert graph = G(n,m)
edgesNum = int(scipy.special.binom(len(original_nodes), 2)*0.0628)
gilbert = gnm_random_graph(len(original_nodes), edgesNum, seed=None, directed=False)
# print('number of nodes G(n,m):', gilbert.number_of_nodes())
# print("number of edges G(n,m):", edgesNum)
# nx.draw(gilbert, node_size=30, node_color='orange')
# plt.show()


# configuration
degrees = []
degree_list = original.degree(original_nodes)
for d in degree_list:
    degrees.append(d[1])

CM = nx.configuration_model(degrees, create_using=None, seed=None)
# pos = nx.spring_layout(CM)
# nx.draw(CM, with_labels=False,  node_size=30, node_color='Brown')
# plt.show()
# print("num nodes of configuration_model:", len(list(CM.nodes)))
# print("num of edges configuration_model:", len(list(CM.edges)))

#--------------------------------------------------------------------------------------------------------------#

degree_sequence = sorted([d for n, d in gilbert.degree()], reverse=True)  # degree sequence
print("degree", (sum(degree_sequence) / len(degree_sequence)))
degreeCount = collections.Counter(degree_sequence)
deg, cnt = zip(*degreeCount.items())
fig, ax = plt.subplots()
plt.bar(deg, cnt, width=0.80, color="brown")
plt.title("Degree Histogram")
plt.ylabel("Count")
plt.xlabel("Degree")
plt.yscale('linear')
plt.xscale('linear')
plt.show()


# connected component:
num_cc = nx.number_connected_components(gilbert)
print("Number of connected components:", num_cc)
largest_cc = max(nx.connected_components(gilbert), key=len) #largest connected component
lccGraph = gilbert.subgraph(largest_cc)
nodes = list(lccGraph.nodes)
edges = list(lccGraph.edges)
# Find the longest shortest path from the node
sour = random.choice(nodes)
print(sour)
shortest_paths = nx.shortest_path(lccGraph, source=sour)
target = max(shortest_paths, key=lambda i: len(shortest_paths[i]))
l_s_path = shortest_paths[target]
l_s_path_edges = list(zip(l_s_path, l_s_path[1:]))

# diameter of the cc_graph:
shortest = shortest_path_length(lccGraph, source=sour)
avg = nx.average_shortest_path_length(lccGraph)
print("sh: ", len(shortest))
print(avg)
print('diameter: ', nx.diameter(lccGraph))


# Draw the graph, then draw over the required edges in red.https://sce-ac-il.zoom.us/j/84506653826
# pos = nx.spring_layout(original)
# nx.draw(gilbert, pos=pos, with_labels=True)
# nx.draw_networkx_edges(gilbert, edge_color='r', edgelist=l_s_path_edges, pos=pos)
# plt.show()
# print("ls:", l_s_path_edges)

