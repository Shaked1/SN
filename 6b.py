import urllib.request
import io
import zipfile
import csv
import matplotlib.pyplot as plt
import networkx as nx
import community



G = nx.Graph() #our graph
myList = {} #dict: {key = video_id : val = list of tags}
list_t = []

G = nx.Graph() #our graph
myList = {} #dict: {key = video_id : val = list of tags}
list_t = []

with open('try.csv', encoding = 'cp850') as inp: #read file cp850
    csv_reader = csv.reader(inp)
    header = next(csv_reader) #skip on header = title col
    for rows in csv_reader:
        list_t = list(rows[4].split('|'))
        if '[none]' not in list_t:
            myList[rows[0]] = (list_t, rows[2])
            G.add_node(rows[0])

dic_tags = {}
myl = []

for videoID1 in myList:
    for videoID2 in myList:
        myl = []
        if videoID1 != videoID2 and (videoID2, videoID1) not in dic_tags and myList[videoID1][1] != myList[videoID2][1]:
            for tag in myList[videoID1][0]:
                if tag in myList[videoID2][0]:
                    myl.append(tag)
                    dic_tags.update({(videoID1, videoID2): myl})
            if len(myl) != 0 :
                G.add_edge(videoID1, videoID2, weight=len(myl))


options = {
    "node_color": "black",
    "node_size": 50,
    "linewidths": 0,
    "width": 0.1,
}
original_nodes = list(G.nodes)
original_edges = list(G.edges)
print("number of nodes ", len(original_nodes))
print("number of edges ", len(original_edges))
# pos = nx.spring_layout(G, seed=1969)  # Seed for reproducible layout
# nx.draw(G, pos,**options)
# plt.show()
color_map = []
t0 = []
t1 = []
t2 = []
t3 = []
t4 = []
t5 = []
t6 = []
t7 = []
t8 = []
t9 = []
t10 = []
t11 = []
t12=[]
t13=[]
t14=[]
#for k, v in nx.get_node_attributes(G, 'value').items():
for k,v in myList.items():

    if v[1] == '1':

        color_map.append('gray')
        t0.append((k,len(v[0])))
    elif v[1] == '2':
        color_map.append('blue')
        t1.append((k,len(v[0])))
    elif v[1] == '10':
        color_map.append('green')
        t2.append((k,len(v[0])))
    elif v[1] == '15':
        color_map.append('red')
        t3.append((k,len(v[0])))
    elif v[1] == '17':
        color_map.append('#fff001')
        t4.append((k,len(v[0])))
    elif v[1] == '19':
        color_map.append('pink')
        t5.append((k,len(v[0])))
    elif v[1] == '20':
        color_map.append('orange')
        t6.append((k,len(v[0])))
    elif v[1] == '22':
        color_map.append('purple')
        t7.append((k,len(v[0])))
    elif v[1] == '23':
        color_map.append('#6f3333')
        t8.append((k,len(v[0])))
    elif v[1] == '24':
        color_map.append('#413088')
        t9.append((k,len(v[0])))
    elif v[1] == '25':
        color_map.append('#30d0e2')
        t10.append((k,len(v[0])))
    elif v[1] == '26':
        color_map.append('#2ff111')
        t11.append((k,len(v[0])))
    elif v[1] == '27':
        color_map.append('#98F5FF')
        t12.append((k,len(v[0])))
    elif v[1] == '28':
        color_map.append('#6495ED')
        t13.append((k,len(v[0])))
    elif v[1] == '29':
        color_map.append('#8B6508')
        t14.append((k,len(v[0])))

nx.draw(G, node_color=color_map, with_labels=False)
plt.show()
teams = [t0, t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11,t12,t13,t14]

#print(nx.algorithms.community.modularity(G, teams))
#print(nx.numeric_assortativity_coefficient(G, "value"))


# סכום דרגות
sum = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
number=-1
for t in teams:
    number+=1
    for j in t:
        sum[number]+=j[1]


fig, ax = plt.subplots()
deg = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11,12,13,14]
colors = ["gray", "blue", "green", "red", "#fff001", "pink", "orange", "purple", "#6f3333", "#413088", "#30d0e2", "#2ff111",'#8B6508','#6495ED','#2ff111']
plt.bar(deg, sum, width=0.80, color=colors)
plt.title("Sum of Degrees")
plt.ylabel("sum")
plt.xlabel("team")
# plt.xscale('log')
# plt.yscale('log')
plt.show()



color_map = []
t0 = []
t1 = []
t2 = []
t3 = []
t4 = []
t5 = []
t6 = []
t7 = []
t8 = []
t9 = []
t10 = []
t11 = []
t12=[]
t13=[]
t14=[]
#for k, v in nx.get_node_attributes(G, 'value').items():
for k,v in myList.items():

    if v[1] == '1':

        color_map.append('gray')
        t0.append(k)
    elif v[1] == '2':
        color_map.append('blue')
        t1.append(k)
    elif v[1] == '10':
        color_map.append('green')
        t2.append(k)
    elif v[1] == '15':
        color_map.append('red')
        t3.append(k)
    elif v[1] == '17':
        color_map.append('#fff001')
        t4.append(k)
    elif v[1] == '19':
        color_map.append('pink')
        t5.append(k)
    elif v[1] == '20':
        color_map.append('orange')
        t6.append(k)
    elif v[1] == '22':
        color_map.append('purple')
        t7.append(k)
    elif v[1] == '23':
        color_map.append('#6f3333')
        t8.append(k)
    elif v[1] == '24':
        color_map.append('#413088')
        t9.append(k)
    elif v[1] == '25':
        color_map.append('#30d0e2')
        t10.append(k)
    elif v[1] == '26':
        color_map.append('#2ff111')
        t11.append(k)
    elif v[1] == '27':
        color_map.append('#98F5FF')
        t12.append(k)
    elif v[1] == '28':
        color_map.append('#6495ED')
        t13.append(k)
    elif v[1] == '29':
        color_map.append('#8B6508')
        t14.append(k)

nx.draw(G, node_color=color_map, with_labels=False)
plt.show()
teams = [t0, t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11,t12,t13,t14]

print(nx.algorithms.community.modularity(G, teams))

#----------------- football--------------------------
import urllib.request
import io
import zipfile

import matplotlib.pyplot as plt
import networkx as nx

url = "http://www-personal.umich.edu/~mejn/netdata/football.zip"

sock = urllib.request.urlopen(url)  # open URL
s = io.BytesIO(sock.read())  # read into BytesIO "file"
sock.close()

zf = zipfile.ZipFile(s)  # zipfile object
txt = zf.read("football.txt").decode()  # read info file
gml = zf.read("football.gml").decode()  # read gml data
# throw away bogus first line with # from mejn files
gml = gml.split("\n")[1:]
G = nx.parse_gml(gml)  # parse gml data
print(txt)
# # print degree for each team - number of games
# for n, d in G.degree():
#     print(f"{n:20} {d:2}")

options = {
    "node_color": "black",
    "node_size": 50,
    "linewidths": 0,
    "width": 0.1,
}
original_nodes = list(G.nodes)
original_edges = list(G.edges)
print("number of nodes ", len(original_nodes))
print("number of edges ", len(original_edges))
# pos = nx.spring_layout(G, seed=1969)  # Seed for reproducible layout
# nx.draw(G, pos,**options)
# plt.show()
color_map = []
t0 = []
t1 = []
t2 = []
t3 = []
t4 = []
t5 = []
t6 = []
t7 = []
t8 = []
t9 = []
t10 = []
t11 = []
for k, v in nx.get_node_attributes(G, 'value').items():
    print(k, v)
    if v == 0:
        color_map.append('gray')
        t0.append(k)
    elif v == 1:
        color_map.append('blue')
        t1.append(k)
    elif v == 2:
        color_map.append('green')
        t2.append(k)
    elif v == 3:
        color_map.append('red')
        t3.append(k)
    elif v == 4:
        color_map.append('#fff001')
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
    elif v == 8:
        color_map.append('#6f3333')
        t8.append(k)
    elif v == 9:
        color_map.append('#413088')
        t9.append(k)
    elif v == 10:
        color_map.append('#30d0e2')
        t10.append(k)
    elif v == 11:
        color_map.append('#2ff111')
        t11.append(k)
nx.draw_circular(G, node_color=color_map, with_labels=False)
plt.show()
t = [t0, t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11]

print(nx.algorithms.community.modularity(G, t))
print(nx.numeric_assortativity_coefficient(G, "value"))


# סכום דרגות
sum = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
degrees = list(G.degree())
l = list(G.nodes.data("value"))
print(degrees)
print(l)
for i in range(len(l)):
    sum[l[i][1]-1] += degrees[i][1]
print(sum)
fig, ax = plt.subplots()
deg = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
colors = ["gray", "blue", "green", "red", "#fff001", "pink", "orange", "purple", "#6f3333", "#413088", "#30d0e2", "#2ff111"]
plt.bar(deg, sum, width=0.80, color=colors)
plt.title("Sum of Degrees")
plt.ylabel("sum")
plt.xlabel("team")
# plt.xscale('log')
# plt.yscale('log')
plt.show()
