import networkx as nx
import matplotlib.pyplot as plt
import csv
import random
import collections
from networkx import shortest_path_length


G = nx.Graph() #our graph
myList = {} #dict: {key = video_id : val = list of tags}
list_t = []

with open('try.csv', encoding = 'cp850') as inp: #read file cp850
    csv_reader = csv.reader(inp)
    header = next(csv_reader) #skip on header = title col
    for rows in csv_reader:
        list_t = list(rows[4].split('|'))
        if '[none]' not in list_t:
            myList[rows[0]] = list_t
            G.add_node(rows[0])


# print(myList.items())
dic_tags = {}
myl = []

for videoID1 in myList:
    for videoID2 in myList:
        myl = []
        if videoID1 != videoID2 and (videoID2, videoID1) not in dic_tags:
            for tag in myList[videoID1]:
                if tag in myList[videoID2]:
                    myl.append(tag)
                    dic_tags.update({(videoID1, videoID2): myl})
            if len(myl) != 0:
                G.add_edge(videoID1, videoID2, label=len(myl))

# print(G.edges)
# print(dic_tags.items())

# print(len(dic_tags.items())) #232813 -> 217626
#
# print(G.number_of_edges()) #26487
# print(G.number_of_nodes()) #1115

# plt.axis('off')
pos = nx.spring_layout(G)
# edge_labels = nx.get_edge_attributes(G, 'label')
# nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, label_pos=0.9, font_color='red', font_size=16)
# nx.draw(G, pos)
# plt.show()


print('\nNumber of connected components: ', nx.number_connected_components(G)) #number of connected components
largest_cc = max(nx.connected_components(G), key=len) #largest connected component
lccGraph = G.subgraph(largest_cc)
nodes = list(lccGraph.nodes)
edges = list(lccGraph.edges)
print('Betweenness centrality:\n', nx.betweenness_centrality(lccGraph)) #betweenness centrality


# nx.draw(lccGraph)
# plt.show()
# print('nodes: ', len(nodes))
# print('edges: ', len(edges))
# # print('diameter: ', nx.diameter(lccGraph))
# shortest = shortest_path_length(lccGraph, source= random.choice(nodes))
# avg = nx.average_shortest_path_length(lccGraph)
# print("sh: ", len(shortest))
# print(avg)
# degree_sequence = sorted([d for n, d in lccGraph.degree()], reverse=True)  # degree sequence
# print("degree", (sum(degree_sequence) / len(degree_sequence)))
# degreeCount = collections.Counter(degree_sequence)
# deg, cnt = zip(*degreeCount.items())
# fig, ax = plt.subplots()
# plt.bar(deg, cnt, width=2.5, color="pink")
# plt.title("Degree Histogram")
# plt.ylabel("Count")
# plt.xlabel("Degree")
# plt.yscale('linear')
# plt.xscale('linear')
# plt.show()

print('\nDegree centrality:\n', sorted(nx.degree_centrality(lccGraph), reverse= False)) #degree centrality
print(nx.degree_centrality(lccGraph))

shortest = shortest_path_length(lccGraph, source= random.choice(nodes))
avg = nx.average_shortest_path_length(lccGraph)
print("sh: ", len(shortest))
print(avg)

# Pick a random node
source = random.choice(list(lccGraph.nodes))
# # Find the longest shortest path from the node
shortest_paths = nx.shortest_path(lccGraph, source=source)
target = max(shortest_paths, key=lambda i: len(shortest_paths[i]))
l_s_path = shortest_paths[target]
l_s_path_edges = list(zip(l_s_path, l_s_path[1:]))

# Draw the graph, then draw over the required edges in red.
pos = nx.spring_layout(G)
nx.draw(G, pos=pos, with_labels=True)
nx.draw_networkx_edges(G, edge_color='r', edgelist=l_s_path_edges, pos=pos)
plt.show()

print('Betweenness centrality:\n', nx.betweenness_centrality(lccGraph)) #betweenness centrality
print('closeness centrality:\n', nx.closeness_centrality()) #katz centrality








