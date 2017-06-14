import pandas as pd
topo=pd.read_excel("./data/Topo_75.xlsx","Sheet1")
src_No = topo["src.No"]
# src_No = topo["src_No"][8]
print(src_No)
print(src_No[8])
print(type(src_No[8]))
i=21
print(type(i))