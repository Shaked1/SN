import csv
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
from networkx import info, edge_betweenness_centrality

# G = nx.Graph() #our graph
# myList = {} #dict: {key = video_id : val = list of tags}
# list_t = []
#
# with open('try.csv', encoding = 'cp850') as inp: #read file cp850
#     csv_reader = csv.reader(inp)
#     header = next(csv_reader) #skip on header = title col
#     for rows in csv_reader:
#         list_t = list(rows[4].split('|'))
#         if '[none]' not in list_t:
#             myList[rows[0]] = (list_t, rows[2])
#             G.add_node(rows[0])
#
# dic_tags = {}
# myl = []
#
# for videoID1 in myList:
#     for videoID2 in myList:
#         myl = []
#         if videoID1 != videoID2 and (videoID2, videoID1) not in dic_tags and myList[videoID1][1] == myList[videoID2][1]:
#             for tag in myList[videoID1][0]:
#                 if tag in myList[videoID2][0]:
#                     myl.append(tag)
#                     dic_tags.update({(videoID1, videoID2): myl})
#             if len(myl) != 0:
#                 G.add_edge(videoID1, videoID2, weight=len(myl))

Data = open('stormofswords.csv', "r")
next(Data, None)  # skip the first line in the input file
GraphType = nx.Graph()
original = nx.parse_edgelist(Data, delimiter=',', create_using=GraphType, nodetype=str, data=(('weight', float),))
G = original
giantGraph = G.subgraph(max(nx.connected_components(G), key=len)) #largest connected component
unfrozen_graph = nx.Graph(giantGraph) #need be unfrozen to work and change him.

edges = sorted(giantGraph.edges(data=True), key=lambda t: t[2].get('weight', 1), reverse=True)
# edges = giantGraph.edges()
print(edges)
union = []
cut = []
neighborhoodOverlap = []
weight = []
for u, v, w in edges:
    for key in w:
        l1 = giantGraph[u] # list of neighborhood of u
        l2 = giantGraph[v] # list of neighborhood of v
        cut = list(set(l1).intersection(l2))
        union = list(set(l1) | set(l2))
        neighborhoodOverlap.append(len(cut) / len(union))
        weight.append(w[key])

plt.plot(weight, neighborhoodOverlap, 'o', mfc='none')
plt.xlabel('Edge Weight')
plt.ylabel('Neighborhood overlap')
plt.title('Neighborhood Overlap As Function Weight')
plt.show()

numOfEdgesRemoved = 0
giantSize_edgesRemoved = []

#removed edges weak to strong
weak2strong = sorted(unfrozen_graph.edges(data=True), key=lambda t: t[2].get('weight', 1))
x1 = []
y1 = []
for edge in weak2strong:
    if edge in unfrozen_graph.edges:
        unfrozen_graph.remove_edge(edge[0], edge[1]) # remove edge
        numOfEdgesRemoved += 1 # count number of edges removed
        unfrozen_graph = nx.Graph(unfrozen_graph.subgraph(max(nx.connected_components(unfrozen_graph), key=len))) #update giant cc
        x1.append(numOfEdgesRemoved)
        y1.append(unfrozen_graph.number_of_nodes())

plt.plot(x1, y1, color ='blue', label = 'Weak to Strong')
plt.xlabel('Number of edges removed')
plt.ylabel('Giant Component Size')
plt.title('Weak to Strong')
plt.show()

# removed edges strong to weak
Data = open('stormofswords.csv', "r")
next(Data, None)  # skip the first line in the input file
GraphType = nx.Graph()
original = nx.parse_edgelist(Data, delimiter=',', create_using=GraphType, nodetype=str, data=(('weight', float),))
G = original
giantGraph = G.subgraph(max(nx.connected_components(G), key=len)) #largest connected component
unfrozen_graph = nx.Graph(giantGraph) #need be unfrozen to work and change him.
strong2weak = sorted(unfrozen_graph.edges(data=True), key=lambda t: t[2].get('weight', 1), reverse= True)
print(strong2weak)
x2 = []
y2 = []
for edge in strong2weak:
    if edge in unfrozen_graph.edges:
        unfrozen_graph.remove_edge(edge[0], edge[1]) # remove edge
        numOfEdgesRemoved += 1 # count number of edges removed
        unfrozen_graph = nx.Graph(unfrozen_graph.subgraph(max(nx.connected_components(unfrozen_graph), key=len))) #update giant cc
        x2.append(numOfEdgesRemoved)
        y2.append(unfrozen_graph.number_of_nodes())
#
print(x1, '\n', x2)
# plt.plot(x2, y2, color ='green', label = 'Strong to Weak')
# plt.xlabel('Number of edges removed')
# plt.ylabel('Giant Component Size')
# plt.title('Strong to Weak')
# plt.show()

# removed edges Betweenness Order
# giantGraph = G.subgraph(max(nx.connected_components(G), key=len)) #largest connected component
# unfrozen_graph = nx.Graph(giantGraph) #need be unfrozen to work and change him.
x3 = []
y3 = []
# edge_betweenness = sorted(edge_betweenness_centrality(giantGraph), key=lambda item: item[1])
# print(len(edge_betweenness))
# for edge in edge_betweenness:
#     unfrozen_graph.remove_edge(edge[0], edge[1])  # remove edge
#     numOfEdgesRemoved += 1  # count number of edges removed
#     unfrozen_graph = nx.Graph(
#         unfrozen_graph.subgraph(max(nx.connected_components(unfrozen_graph), key=len)))  # update giant cc
#     edge_betweenness = sorted(edge_betweenness_centrality(unfrozen_graph), key=lambda item: item[1])
#     x3.append(numOfEdgesRemoved)
#     y3.append(unfrozen_graph.number_of_nodes())
#
# plt.plot(x3, y3, color ='red', label = 'Betweenness Order')
plt.plot(x1, y1, x2, y2)
# plt.plot(x1, y1, color ='blue', label = 'Betweenness Order')
# plt.plot(x2, y2, color ='green', label = 'Betweenness Order')
#
# plt.xlabel('Number of edges removed')
# plt.ylabel('Giant Component Size')
# plt.title('Betweenness Order')
plt.show()





