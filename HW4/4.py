import math
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import powerlaw
import csv

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


GQ2 = nx.barabasi_albert_graph(len(nodes), int(len(edges)/len(nodes)))
pos = nx.spring_layout(GQ2, k=0.1)
nx.draw_networkx(GQ2, pos, with_labels=False, node_size=10, node_color='orange')
plt.show()

G_su = lccGraph
G_su1 = GQ2
degree_sequence = sorted([d for n, d in G_su.degree()], reverse=True) # used for degree distribution and powerlaw test
fit = powerlaw.Fit(degree_sequence, xmin=1)


fig2 = fit.plot_pdf(color='b', linewidth=2)
fit.power_law.plot_pdf(color='g', linestyle='--', ax=fig2)
plt.show()
R, p = fit.distribution_compare('power_law', 'exponential', normalized_ratio=True)
print(R, p)

plt.figure(figsize=(10, 6))
fit.distribution_compare('power_law', 'lognormal')
fig4 = fit.plot_ccdf(linewidth=3, color='black')
fit.power_law.plot_ccdf(ax=fig4, color='r', linestyle='--') #powerlaw
fit.lognormal.plot_ccdf(ax=fig4, color='g', linestyle='--') #lognormal
fit.stretched_exponential.plot_ccdf(ax=fig4, color='b', linestyle='--') #stretched_exponential
plt.show()


# ass 4
#Question1

def plot_degree_dist(G):
    degrees = [G.degree(n) for n in G.nodes()]
    plt.hist(degrees, color='blue')
    plt.xlabel('degree')
    plt.ylabel('count')
    plt.title('Degree Distribution ')
    plt.show()

plot_degree_dist(G_su1)


degs = {}
for n in G_su1.nodes():
    deg = G_su1.degree(n)
    if deg not in degs:
        degs[deg] = 0
    degs[ deg ] += 1

items = sorted(degs.items())
#items = sorted(degs.items())
fig = plt.figure ()
ax = fig .add_subplot ()
ax.plot ([ k for (k , v ) in items ] , [ v for (k ,v ) in items ])
ax.set_xscale ('log')
ax.set_yscale ('log')
plt.title ( "Degree Distribution" )
plt.show()
print(nx.info(G_su1))


k = []
Pk = []
logk=[]
logPk=[]

for node in G_su1.nodes():
    degree = G_su1.degree(nbunch=node)
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
plt.title('Degree Distribution')
m, c = np.polyfit(logk_array, logPk_array, 1)
fit = powerlaw.Fit(np.array(logk_array)+1,xmin=1,discrete=True)

print('alpha= ',fit.power_law.alpha,'  sigma= ',fit.power_law.sigma)
print("The Beta:",c)
plt.plot(logk_array, m*logk_array + c, "-")

print("Graph Info: ",nx.info(G_su1))

plt.show()
