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
# 读取数据
topo=pd.read_excel("./data/Topo_75.xlsx","Sheet2")
src_No = list(topo["src.No"])
dst_No = list(topo["dst.No"])
Distance = list(topo["distance"])
Node=pd.read_excel("./data/Topo_75.xlsx","Sheet1")
Node_No = list(Node["Node.No"])
S = len(Node_No) #TODO 节点个数
E = len(src_No) #TODO 链路个数
#添加节点
while i<= S:
    G.add_node(i)
    i+=1
#添加链路
# print(Node_No)
# print(len(src_No))
# print(topo)
while j < E:
    G.add_edge(src_No[j],dst_No[j],length=Distance[j])
    j = j+1
All_Path_list = []  #TODO 双向链路集
j=0
while j<E:
    All_Path_list.append((src_No[j],dst_No[j]))
    All_Path_list.append((dst_No[j],src_No[j]))
    j += 1
# print(All_Path_list)
# nx.draw(G,with_labels=True)  #TODO 将图带标签绘制
# plt.show()
shortest_paths = nx.all_pairs_shortest_path(G,cutoff=None)
shortest_path_length=nx.all_pairs_shortest_path_length(G,cutoff=None)
# print(shortest_paths[1][2])
D_path_len1 = nx.algorithms.shortest_paths.weighted.all_pairs_dijkstra_path_length(G,cutoff=None,weight='length')
D_path_hop1 = nx.algorithms.shortest_paths.weighted.all_pairs_dijkstra_path(G,cutoff=None,weight='length')
# D_path=[[]] * len(src_No)

#         D_path[src_Node-1][dst_Node-1] = nx.algorithms.shortest_paths.weighted.dijkstra_path_length(G,src_Node,dst_Node)
#         src_Node += 1
#         dst_Node += 1
# print(D_path_hop1[1][2])

# print(D_path_len.values([1][2]))
src_Node = 1
dst_Node = 1
D_path_hop=[[0 for col in range(S)] for row in range(S)]
D_path_len=[[0 for col in range(S)] for row in range(S)]

# print(len(D_path_hop1[1][2]))
while src_Node <= S:
    while dst_Node <= S:
        if src_Node != dst_Node:
            D_path_hop[src_Node - 1][dst_Node - 1] = len(D_path_hop1[src_Node][dst_Node])-1
            D_path_len[src_Node - 1][dst_Node - 1] = D_path_len1[src_Node][dst_Node]
        else:
            D_path_hop[src_Node-1][dst_Node-1]=0
            D_path_len[src_Node - 1][dst_Node - 1] = 0
        dst_Node += 1
    src_Node += 1
src_Node = 1
dst_Node = 1
#TODO 节点序数从0到个数减1
path_len_max = np.max(D_path_len)  # TODO 最大长度（拓扑直径）
# print(A)
# print(D_path_hop[0][18]) # TODO 0节点到1节点跳数
# print(D_path_len[0][18]) #TODO 输出点0和点18的最短路径
# print(G.degree(24))

Node_degree = []
for i in range(S):
    Node_degree.append(G.degree(i+1))
# print(len(Node_degree))
# Node_degree[0] #TODO 节点0的度
P_E_F_eta=0.003 #FIXME 单位距离发生故障的概率
P_E_F = [[0 for col in range(S)] for row in range(S)]
while src_Node <= S:
    while dst_Node <= S:
        if src_Node != dst_Node:
            P_E_F[src_Node - 1][dst_Node - 1] = 1 - pow(1-P_E_F_eta,D_path_len[src_Node - 1][dst_Node - 1]/100)
        else:
            P_E_F[src_Node - 1][dst_Node - 1] = 0
        dst_Node += 1
    src_Node += 1
# P_E_F[0][74] #TODO 第0点和第74点的链路故障概率
Areas = {}  #FIXME TODO 分好的域序列,字典形式，详情见dict_test.py中d3构造
def Area_in_Path_Num(Node_list,All_Path_list):  #TODO 域内节点链路判断得出域内链路个数
    """
    :param Node_list: 域内节点序列
    :param All_Path_list: 所有链路序列
    :return: 域内Edge个数
    """
    Path_Num_in = 0
    for i in Node_list:
        for j in Node_list[i+1:]:
            if (i,j) in All_Path_list:
                Path_Num_in += 1
            else:
                Path_Num_in += 0
    return Path_Num_in

def Area_btw_Path_Num(Node_list1,Node_list2,All_Path_list):    #TODO 域间节点链路判断得出域间链路个数
    """
    :param Node_list1: 域1内节点序列
    :param Node_list2: 域2内节点序列
    :param All_Path_list: 所有链路序列
    :return: 域间Edge个数
    """
    Path_Num_btw = 0
    for i in Node_list1:
        for j in Node_list2:
            if (i, j) in All_Path_list:
                Path_Num_btw += 1
            else:
                Path_Num_btw += 0
    return Path_Num_btw


def Abstract_Node_Num(Node_list,All_Node_list,All_Edge_list):  #TODO 输出抽象后的节点列表
    """
    :param Node_list:域内节点序列
    :param All_Node_list: 所有节点序列
    :param All_Edge_list: 所有直连路径序列
    :return: 域内节点抽象后输出的节点列表
    """
    Other_Node_list = All_Node_list-Node_list
    Abstract_Node_list = []
    for NodeinArea in Node_list:
        for NodeinOther in Other_Node_list:
            if ((NodeinArea,NodeinOther) in All_Edge_list) or ((NodeinOther,NodeinArea) in All_Edge_list):
                Abstract_Node_list.append(NodeinArea)
            else:
                Abstract_Node_list.copy()
    return Abstract_Node_list

def P_E_F(Node_list,All_Edge_list,eta):
    """
    :param Node_list: 节点列表
    :param All_Edge_list: 所有的直连链路列表
    :param eta: 单位长度故障率
    :return:
    """


# def Path_Num2Dict()






















# G.add_edge(2,3)
# print(G.nodes())
# print(G.edges())
# plt.show()
# print(nx)