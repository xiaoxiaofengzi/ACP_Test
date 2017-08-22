d1={1:11,2:12,3:13,4:14}
d2  = {1:21,2:22,3:33,5:55}
print(d1.items()+d2.items())
print(dict(d1.items()+d2.items()))
print(dict(d1,**d2))
l = [(1,1),(1,2),(1,3),(1,4)]
print(dict(l))
import pandas as pd
pd.read_csv(names=)