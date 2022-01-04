import networkx as nx
import matplotlib.pyplot as plt

import collections
import numpy as np
from scipy.stats import binom
import scipy.special
import csv
import community


# ייבוא גרף
Data = open('stormofswords.csv', "r")
next(Data, None)  # skip the first line in the input file
Graphtype = nx.Graph()
G = nx.parse_edgelist(Data, delimiter=',', create_using=Graphtype, nodetype=str, data=(('weight', int),))
# print(G.edges(data=True))
original_nodes = list(G.nodes)
original_edges = list(G.edges)
print("number of nodes ", len(original_nodes))
print("number of edges ", len(original_edges))
# print("original_nodes", original_nodes)
# print("original_edges", original_edges)
num_of_nodes = len(original_nodes)
nx.draw(G, with_labels=False)
plt.show()


# הוספת תכונת שבטים
tribes = {}
t = []
partition={}
with open('ASS_tribes.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        tribes[row['node']] = int(row['tribe'])

nx.set_node_attributes(G, tribes, "tribe")
#print(nx.get_node_attributes(G, "tribe"))
#print("#########",tribes)
color_map = []
t1 = []
t2 = []
t3 = []
t4 = []
t5 = []
t6 = []
t7 = []
for k, v in nx.get_node_attributes(G, 'tribe').items():
    # print(k, v)
    if v == 1:
        color_map.append('blue')
        t1.append(k)
    elif v == 2:
        color_map.append('green')
        t2.append(k)
    elif v == 3:
        color_map.append('red')
        t3.append(k)
    elif v == 4:
        color_map.append('yellow')
        t4.append(k)
    elif v == 5:
        color_map.append('pink')
        t5.append(k)
    elif v == 6:
        color_map.append('orange')
        t6.append(k)
    elif v == 7:
        color_map.append('purple')
        t7.append(k)
nx.draw(G, node_color=color_map, with_labels=False, font_size=8)
plt.show()
t = [t1, t2, t3, t4, t5, t6, t7]

#ציור לפי גדלי צמתים
degree_sequence = sorted([d for n, d in G.degree()], reverse=True)
node_sizes=[]
for x in degree_sequence:
    node_sizes.append(x*50)
nx.draw(G, node_color=color_map,node_size=node_sizes, with_labels=False,alpha=0.8)
plt.show()

# ציור עם משקלים
pos=nx.spring_layout(G)
#
# pos=nx.get_node_attributes(G,'pos')
nx.draw(G,pos,with_labels=True,node_color=color_map)
labels = nx.get_edge_attributes(G,'weight')
nx.draw_networkx_edge_labels(G,pos,edge_labels=labels,font_size=7,font_color='black')
plt.show()
# #
print(nx.algorithms.community.modularity(G, t))
print(community.community_louvain.modularity(tribes,G))
print(nx.numeric_assortativity_coefficient(G, "tribe"))



#סכום דרגות
sum=[0,0,0,0,0,0,0]
degrees = list(G.degree())
l=list(G.nodes.data("tribe"))

for i in range(len(l)):
    sum[l[i][1]-1]+=degrees[i][1]

fig, ax = plt.subplots()
deg=[1,2,3,4,5,6,7]
colors=["blue","green","red","yellow","pink","orange","purple"]
plt.bar(deg, sum, width=0.80, color=colors)
plt.title("Sum of Degrees")
plt.ylabel("sum")
plt.xlabel("tribe")
# plt.xscale('log')
# plt.yscale('log')
plt.show()