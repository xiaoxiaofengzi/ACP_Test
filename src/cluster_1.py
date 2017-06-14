import networkx as nx
import matplotlib.pyplot as plt
import math

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
#添加节点
while i<= 75:
    G.add_node(i)
    i+=1
#添加链路
G.add_edge(2,3)
print(G.nodes())
print(G.edges())
plt.show()
# print(nx)