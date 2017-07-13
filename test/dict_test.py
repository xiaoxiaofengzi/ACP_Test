# import radiansdict

# print(pow(2,0.5)
d1 = {1:[]}
print(d1[1])
d1[1].append(1)
print(d1[1])
print("二维字典\n")
d2 = {1:{1:[]}}
print(d2[1][1])
d2[1][1].append(1)
print(d2[1][1])
print(d2[1][1][0])
d2[1][2]=[2]
print(d2)
d3 = {1:[],3:[]}
d3[3]=d2
d3[3][1][2].append(0)
print(d3)  #TODO 控制器节点归属表示方法，即域划分结果表示
print(d3[3][1][1]+d3[3][1][2])
print(type(d3[3][1][1]))
if type(d3[3][1][1]) == list:
    print("True")
else:
    print("false")
d4 = d3.copy()
print("d4 is ",d4)

d5 = d3[3][1].items()
print("d5 is ",d5)