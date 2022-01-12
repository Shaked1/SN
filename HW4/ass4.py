#ASS -04
import networkx as nx
import matplotlib.pyplot as plt
import collections
import numpy as np
import powerlaw
import csv
import math

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

largest_cc = max(nx.connected_components(G), key=len) #largest connected component
lccGraph = G.subgraph(largest_cc)
nodes = list(lccGraph.nodes)
edges = list(lccGraph.edges)

G = lccGraph


# ass 4
# Question1

# GQ2 = nx.barabasi_albert_graph(len(nodes), int(len(edges)/len(nodes)))
# pos = nx.spring_layout(GQ2, k=0.1)
# nx.draw_networkx(GQ2, pos, with_labels=False, node_size=10, node_color='orange')
# plt.show()
GQ2 = lccGraph

def plot_degree_dist(G):
    degrees = [G.degree(n) for n in G.nodes()]
    plt.hist(degrees, color='blue')
    plt.xlabel('degree')
    plt.ylabel('count')
    plt.yscale('linear')
    plt.xscale('linear')
    plt.title('Degree Distribution')
    plt.show()

plot_degree_dist(GQ2)

# היסטוגרמת דרגות
degree_sequence = sorted([d for n, d in GQ2.degree()], reverse=True)  # degree sequence
degreeCount = collections.Counter(degree_sequence)
deg, cnt = zip(*degreeCount.items())
fig, ax = plt.subplots()
plt.bar(deg, cnt, width=0.80, color="blue")
plt.title("Degree Histogram Linear X Log Y")
plt.ylabel("Count")
plt.xlabel("Degree")
plt.xscale('linear')
plt.yscale('log')
plt.show()


degrees = {}
for n in GQ2.nodes():
    deg = GQ2.degree(n)
    if deg not in degrees:
        degrees[deg] = 0
    degrees[deg] += 1

items = sorted(degrees.items())
fig = plt.figure()
ax = fig .add_subplot()
ax.plot([k for (k, v) in items], [v for (k, v) in items], color= 'blue')
plt.title("Degree Distribution")
plt.show()


k = []
Pk = []
logk = []
logPk = []

for node in GQ2.nodes():
    degree = GQ2.degree(nbunch=node)
    try:
        pos = k.index(degree)
    except ValueError as e:
        k.append(degree)
        Pk.append(1)
    else:
        Pk[pos] += 1

# get a double log representation
for i in range(len(k)):
    logk.append(math.log10(k[i]))
    logPk.append(math.log10(Pk[i]))

order = np.argsort(logk)
logk_array = np.array(logk)[order]
logPk_array = np.array(logPk)[order]
plt.plot(logk_array, logPk_array, ".")
plt.xlabel('log of degree k')
plt.ylabel('frequency of P(k)')
plt.title('Degree Distribution')
m, c = np.polyfit(logk_array, logPk_array, 1)
fit = powerlaw.Fit(np.array(logk_array)+1, xmin=1, discrete=True)

print('alpha= ', fit.power_law.alpha, '  sigma= ', fit.power_law.sigma)
print("The Beta:", c)
plt.plot(logk_array, m*logk_array + c, "-")
plt.show()

