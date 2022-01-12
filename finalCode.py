import networkx as nx
import csv
import matplotlib.pyplot as plt

G = nx.Graph()  # our graph
myDB = {}  # dict: {key = video_id : val = (list of tags), category_id, views}

# open and read dataset file #
with open('YouTubeDB.csv', encoding='cp850') as inp:
    csv_reader = csv.reader(inp)
    header = next(csv_reader)  # skip on header = title col
    for rows in csv_reader:
        list_t = list(rows[4].split('|'))
        if '[none]' not in list_t: # only video with tags
            myDB[rows[0]] = (list_t, rows[2], int(rows[5]))
            G.add_node(rows[0])


# create graph according myDB #
dic_tags = {}
commonsTags = [] # list of common tags between v1 and v2
w = {} # dict: {key: edge, value: weight edge, views of v1, views of v2}
for videoID1 in myDB:
    for videoID2 in myDB:
        commonsTags = []
        if videoID1 != videoID2 and (videoID2, videoID1) not in dic_tags:
            for tag in myDB[videoID1][0]:
                if tag in myDB[videoID2][0]:
                    commonsTags.append(tag)
                    dic_tags.update({(videoID1, videoID2): commonsTags})
            if len(commonsTags) > 0: # videoID1, videoID2 have common tag
                weightEdge = len(commonsTags) / min(len(myDB[videoID1][0]), len(myDB[videoID2][0]))
                w[(videoID1, videoID2)] = [weightEdge, myDB[videoID1][2], myDB[videoID2][2]]
                G.add_edge(videoID1, videoID2, weight = weightEdge)

# original graph #
print('Number of nodes: ', len(G.nodes)) # 1115
print('Number of edges: ', len(G.edges)) # 26487
nx.draw_networkx_edge_labels(G, nx.spring_layout(G), edge_labels = nx.get_edge_attributes(G, 'weight'), label_pos=0.9, font_color='black', font_size=10)
nx.draw(G, nx.spring_layout(G))
plt.show()

# connected components #
print('Number of connected components: ', nx.number_connected_components(G)) # 96
lccGraph = G.subgraph(max(nx.connected_components(G), key=len)) # The largest connected component
print('Number of nodes of lcc: ', len(lccGraph.nodes)) # 1013
print('Number of edges of lcc: ', len(lccGraph.edges)) # 26480
print('Diameter: ', nx.diameter(lccGraph)) # diameter = 7
print('Betweenness Centrality of nodes:\n', nx.betweenness_centrality(lccGraph)) # betweenness centrality

# Analysis #
# tags as func of views per video
sort = sorted(myDB.values(), key = lambda t: len(t[0]), reverse=True) # sorted by amount of tags per video
listOfTags = []
listOfViews = []
for v in sort:
    listOfTags.append(len(v[0]))
    listOfViews.append(v[2])
plt.plot(listOfTags, listOfViews, color="#d95b47")
plt.show()

# common tags as func of different view between v1, v2
tempList = []
for edge in w:
    tempList.append((w[edge][0], abs(w[edge][1] - w[edge][2])))
sort = sorted(tempList, key = lambda t: t[0], reverse=True)
commonTags = []
diffViews = []
for e in sort:
    commonTags.append(e[0])
    diffViews.append(e[1])
plt.plot(commonTags, diffViews, 'o', color="#d95b47")
plt.show()

# degree centrality as func of view per video
tempList = []
degreeOfVideo = G.degree
degree = []
view = []
for key in myDB:
    for n in degreeOfVideo:
        if key == n[0]:
            tempList.append([n[0], n[1], int(myDB[key][2])])
            degree.append(int(myDB[key][2]))
            view.append(n[1])

sort = sorted(tempList, key=lambda t: t[1], reverse=True)
d = []
v = []
for i in sort:
    d.append(i[1])
    v.append(i[2])
plt.plot(d, v, color="#d95b47")
plt.show()
