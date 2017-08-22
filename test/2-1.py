l = raw_input().split()
n = len(l)
if n!=4:
    print(-1)
for i in range(n):
    l[i]=int(l[i])
x = l[0]
f = l[1]
d = l[2]
p = l[3]
if d/x<f:
    print(int(d/x))
else:
    print(int((d-f*x)/(p+x))+f)
# s = [0]*n
# m = []
# for i in range(n):
#     m[i] = sorted(l[i])

