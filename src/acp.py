# -*- coding:utf-8 -*-

import networkx as nx
import matplotlib.pyplot as plt
import math
import numpy as np
import pandas as pd
from collections import defaultdict
from heapq import *

# D 算法
P_E_F_eta=0.005 #FIXME the probability of unit distance failure
# 拓扑生成

G = nx.Graph()
i = 1
j = 0
M = 99999999999   # TODO 默认距离无限大
topo=pd.read_excel("./data/Topo_10.xlsx","Sheet2")
src_No = list(topo["src.No"])
dst_No = list(topo["dst.No"])
Distance = list(topo["distance"])
Node=pd.read_excel("./data/Topo_10.xlsx","Sheet1")
Node_No = list(Node["Node.No"])
S = len(Node_No) #TODO the num of node
E = len(src_No) #TODO the num of edge
def dijkstra_raw(edges, from_node, to_node):
    g = defaultdict(list)
    for l, r, c in edges:
        g[l].append((c, r))
    q, seen = [(0, from_node, ())], set()
    while q:
        (cost, v1, path) = heappop(q)
        if v1 not in seen:
            seen.add(v1)
            path = (v1, path)
            if v1 == to_node:
                return cost, path
            for c, v2 in g.get(v1, ()):
                if v2 not in seen:
                    heappush(q, (cost + c, v2, path))
    return float("inf"), []


def dijkstra(edges, from_node, to_node):
    len_shortest_path = -1
    ret_path = []
    length, path_queue = dijkstra_raw(edges, from_node, to_node)
    if len(path_queue) > 0:
        len_shortest_path = length  ## 1. Get the length firstly;
        ## 2. Decompose the path_queue, to get the passing nodes in the shortest path.
        left = path_queue[0]
        ret_path.append(left)  ## 2.1 Record the destination node firstly;
        right = path_queue[1]
        while len(right) > 0:
            left = right[0]
            ret_path.append(left)  ## 2.2 Record other nodes, till the source-node.
            right = right[1]
        ret_path.reverse()  ## 3. Reverse the list finally, to make it be normal sequence.
    return len_shortest_path, ret_path



# Add the list of node
while i<=S:
    G.add_node(i)
    i += 1
# Add the list of edge
while j<E:
    G.add_edge(src_No[j],dst_No[j],length=Distance[j])
    j += 1
# TODO 创造二维矩阵表示拓扑
M_Topo = np.array([[M for col in range(S)] for row in range(S)])
for e in range(E):
    # print(src_No[j])
    # print(dst_No[j])
    # print(Edge[src_No[j]][dst_No[j]])
    M_Topo[src_No[e]-1][dst_No[e]-1] = Distance[e]
    M_Topo[dst_No[e]-1][src_No[e]-1] = Distance[e]
# print(Edge[18][0])  # TODO 点的序列为0~S-1

### --- Read the topology, and generate all edges in the given topology.
edges = []  # TODO 带权重
for i in range(S):
    for j in range(S):
        if i != j and M_Topo[i][j] != M:
            edges.append((i, j, M_Topo[i][j]))  ### (i,j) is a link; M_topo[i][j] here is 1, the length of link (i,j).
latency = np.array([[0 for col in range(S)] for row in range(S)])
# shortest_path = np.array([[0 for col in range(S)] for row in range(S)])
for i in range(S):
    for j in range(S):
        # if i != j and M_Topo[i][j] != M:
        latency[i][j]= dijkstra(edges, i, j)[0]
# print latency
max_lantency = np.amax(latency)
# print max_lantency
def Latency(c):
    """
    :param c:控制器部署位置
    :return: 正规化的平均时延
    """
    delay = 0.0
    for i in range(S):
        delay += latency[i][c]
    # print delay/(max_lantency*29)
    return delay/(max_lantency*(S-1))
# print Latency(26)
Edges = []  # TODO 不带权重
for i in range(S):
    for j in range(S):
        if i != j and M_Topo[i][j] != M:
            Edges.append([i, j])  ### (i,j) is a link; M_topo[i][j] here is 1, the length of link (i,j).

# print "=== Dijkstra ==="
# print "Let's find the shortest-path from 0 to 9:"
# length, Shortest_path = dijkstra(edges, 0, 74)
# print 'length = ', length
# print 'The shortest path is ', Shortest_path


# Add the list of Bi edge
All_Path_list = []  #TODO Bidirectional link set
j=0
while j<E:
    All_Path_list.append((src_No[j],dst_No[j]))
    All_Path_list.append((dst_No[j],src_No[j]))
    j += 1

# print(D_path_hop[1][18])
#TODO the index of node is 0~num(Node)-1

# Add the degree of nodes
Node_degree = []
for i in range(S):
    Node_degree.append(G.degree(i+1))

# The probability of each path failure

P_E_F = [[0 for col in range(S)] for row in range(S)]
# while src_Node <= S:
#     while dst_Node <= S:
#         if src_Node != dst_Node:
#             P_E_F[src_Node - 1][dst_Node - 1] = 1 - pow(1-P_E_F_eta,D_path_len[src_Node - 1][dst_Node - 1]/100)
#         else:
#             P_E_F[src_Node - 1][dst_Node - 1] = 0
#         dst_Node += 1
#     src_Node += 1
def D_to_i(i):
    """
    :param i: 控制器部署位置
    :return: 控制通道路径
    """
    path = []
    d = 0
    while d<S: # FIXME 75为点的个数
        if d != i:
            length, Shortest_path = dijkstra(edges, i, d)
            path.append(Shortest_path)
        d+=1
    return path
# print(D_to_i(1))
def list_in_list(l_sh,l_lo):  # TODO 判定[a,b]是否在[q,v,v,v,v,v,v]中
    n = len(l_lo)
    flag = 0
    for i in range(n-1):
        if l_sh[0]==l_lo[i] and l_sh[1]==l_lo[i+1]:
            flag += 1
        else:
            flag = flag
    return flag>=1

for f in range(E):
    length, Shortest_path = dijkstra(edges, src_No[f]-1, dst_No[f]-1)
    P_E_F[src_No[f]-1][dst_No[f]-1] = 1 - pow(1-P_E_F_eta,length/100)
    P_E_F[dst_No[f] - 1][src_No[f] - 1] = 1 - pow(1 - P_E_F_eta, length / 100)


def P_E_Num(i,j,controler_place):
    """
    :param i:src_node_index [0~74]
    :param j: dst_node_index
    :param P_E: the matrix of P_E_F
    :return:造成瘫痪的节点个数
    """
    length, Shortest_path = dijkstra(edges, i, j)
    l = D_to_i(controler_place)
    # n = len(l)
    A = set()
    if [i,j] in Edges:
        for s in range(len(l)):
            if list_in_list([i,j],l[s]):
                A = set(l[s][l[s].index(j):]) | A
            elif list_in_list([j,i],l[s]):
                A = set(l[s][l[s].index(i):]) | A
            else:
                A = A
        return len(A)
    else:
        return 0

Ept_failure=[0]*S
for c in range(S):
    for i in range(S-1):
        for j in range(S-1):
            if i != j:
                Ept_failure[c] += P_E_F_eta*P_E_Num(i,j,c)
    Ept_failure[c] += P_E_F_eta * P_E_Num(S-1, S-2, c)
    Ept_failure[c] += P_E_F_eta * P_E_Num(S-2, S-1, c)
    Ept_failure[c] /= E
print(Ept_failure)
delay_1 = []
for i in range(S):
    delay_1.append(Latency(i))
print (delay_1)

# bate = 0.1  #FIXME the balance factor

QoS = [0]*S
latency_1 = []
QoS_1 = []
Ept_failure_1 = []
for bate1 in range(11):
    for c in range(S):
        bate = float(bate1)/10
        # print bate
        QoS[c] = bate*Latency(c)/30+(1-bate)*Ept_failure[c]
        # print [Latency(c),Ept_failure[c]]
    controller = QoS.index(min(QoS))
    QoS_1.append(min(QoS))
    latency_1.append(Latency(controller))
    Ept_failure_1.append(Ept_failure[controller])
    print controller
print "QoS_1 is ",QoS_1
print latency_1
print Ept_failure_1
# controller = QoS.index(max(QoS))
# latency_1 = Latency(controller)*max_lantency
# Ept_failure_1 = Ept_failure[controller]









