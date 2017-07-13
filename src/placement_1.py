import networkx as nx
import matplotlib.pyplot as plt
import math
import numpy as np
import pandas as pd

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