import networkx as nx
import matplotlib.pyplot as plt
import math
import numpy as np
import pandas as pd

def distance(lat1,lng1,lat2,lng2):
    '''
    实现经纬度到距离的转换
    :param lat1:纬度1
    :param lng1:经度1
    :param lat2:纬度2
    :param lng2:经度2
    :return:距离
    '''
    radlat1=math.radians(lat1) #转换角度为弧度
    radlat2=math.radians(lat2)
    a=radlat1-radlat2
    b=math.radians(lng1)-math.radians(lng2)
    s=2*math.asin(math.sqrt(math.pow(math.sin(a/2),2)+math.cos(radlat1)*math.cos(radlat2)*math.pow(math.sin(b/2),2)))
    earth_radius=6378.137
    s=s*earth_radius
    if s<0:
        return -s
    else:
        return s

G = nx.Graph()
i = 1
j = 0
#添加节点
while i<= 75:
    G.add_node(i)
    i+=1
#添加链路
topo=pd.read_excel("./data/Topo_75.xlsx","Sheet1")
src_No = list(topo["src.No"])
dst_No = list(topo["dst.No"])
Distance = list(topo["distance"])
# print(len(src_No))
# print(topo)
while j < 99:
    G.add_edge(src_No[j],dst_No[j],length=Distance[j])
    j = j+1
nx.draw(G,with_labels=True)
plt.show()
# G.add_edge(2,3)
# print(G.nodes())
# print(G.edges())
# plt.show()
# print(nx)