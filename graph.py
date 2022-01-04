import networkx as nx
import csv
import matplotlib.pyplot as plt
#import scipy.specia


G = nx.Graph() #our graph
myList = {} #dict: {key = video_id : val = list of tags}
list_t = []
listTags=[]
listView=[]
listTV=[]
with open('database.csv', encoding = 'cp850') as inp: #read file cp850
    csv_reader = csv.reader(inp)
    header = next(csv_reader) #skip on header = title col
    for rows in csv_reader:
        list_t = list(rows[4].split('|'))
        if '[none]' not in list_t:
            myList[rows[0]] = (list_t, rows[2],rows[5])
            G.add_node(rows[0])

dic_tags = {}
myl = []

for videoID1 in myList:
    for videoID2 in myList:
        myl = []
        if videoID1 != videoID2 and (videoID2, videoID1) not in dic_tags and myList[videoID1][1] == myList[videoID2][1]:
            for tag in myList[videoID1][0]:
                if tag in myList[videoID2][0]:
                    myl.append(tag)
                    dic_tags.update({(videoID1, videoID2): myl})
            if len(myl) != 0:
                x= min(len(myl) / len(myList[videoID1][0]), len(myl) / len(myList[videoID2][0]))
                G.add_edge(videoID1, videoID2, weight=x)
                y=max(int(myList[videoID1][2])/int(myList[videoID2][2]),int(myList[videoID2][2])/int(myList[videoID1][2]))
                listTV.append((x,y))
                listTags.append(x)
                listView.append(y)
print(listView)

# print(len(listTags))
# print(listTV)




original_nodes = list(G.nodes)
original_edges = list(G.edges)
print("number of nodes ", len(original_nodes))
print("number of edges ", len(original_edges))


# pos = nx.spring_layout(G)
# edge_labels = nx.get_edge_attributes(G, 'weight')
# nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, label_pos=0.9, font_color='red', font_size=16)
# nx.draw(G, pos)
# plt.show()


#חלוקה של צבעים לפי קטגוריות
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
teams = []
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
        teams.append((k,len(v[0])))

# nx.draw(G, node_color=color_map, with_labels=False)
# plt.show()


#print(nx.algorithms.community.modularity(G, teams))
#print(nx.numeric_assortativity_coefficient(G, "value"))

#850-10,000
#10,000-100,000
#
# גודלצומת הסירטון מושפע לפי כמות הצפיות שיש לאותו סירטון
node_sizes = []
#color_map = []

for k,v in myList.items():

    if v[2] <='12639' and v[2]>='0':
        #color_map.append('gray')
        #t0.append((k,v[2]))
        node_sizes.append(200)
    elif v[2] >'12640' and  v[2] <='22239':
        #color_map.append('blue')
        #t1.append((k,v[2]))
        node_sizes.append(350)
    elif v[2] >'22240' and  v[2] <'48800':
        #color_map.append('green')
        #t2.append((k,v[2]))
        node_sizes.append(500)
    elif v[2] >='48801':
        #color_map.append('red')
        #t3.append((k,v[2]))
        node_sizes.append(2000)
    # elif v[1] == '17':
    #     color_map.append('#fff001')
    #     t4.append((k,v[2]))
    # elif v[1] == '19':
    #     color_map.append('pink')
    #     t5.append((k,v[2]))
    # elif v[1] == '20':
    #     color_map.append('orange')
    #     t6.append((k,v[2]))
    # elif v[1] == '22':
    #     color_map.append('purple')
    #     t7.append((k,v[2]))
    # elif v[1] == '23':
    #     color_map.append('#6f3333')
    #     t8.append((k,v[2]))
    # elif v[1] == '24':
    #     color_map.append('#413088')
    #     t9.append((k,v[2]))
    # elif v[1] == '25':
    #     color_map.append('#30d0e2')
    #     t10.append((k,v[2]))
    # elif v[1] == '26':
    #     color_map.append('#2ff111')
    #     t11.append((k,v[2]))
    # elif v[1] == '27':
    #     color_map.append('#98F5FF')
    #     t12.append((k,v[2]))
    # elif v[1] == '28':
    #     color_map.append('#6495ED')
    #     t13.append((k,len(v[0])))
    # elif v[1] == '29':
    #     color_map.append('#8B6508')
    #     t14.append((k,len(v[0])))


pos = nx.spring_layout(G)
nx.draw_networkx(G,pos,  node_color=color_map,with_labels=False,node_size= node_sizes)
plt.show()


# plotting the points
plt.scatter(listTags,listView,label= "stars", color= "green",marker= "*", s=30)
# naming the x axis
plt.xlabel('tags')
# naming the y axis
plt.ylabel('view')

# giving a title to my graph
plt.title('My first graph!')

# function to show the plot
plt.show()