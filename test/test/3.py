list = raw_input().split()
n = len(list)
for i in range(n):
    list[i]=int(list[i])
k = list[1]
matrix = [[0]*(i+1) for i in range(k)]
i = 1
j = 1
while i<=k:
    while j<=i:
        if i%j != 0:
            matrix[i-1][j-1] = 1
        else:
            matrix[i - 1][j - 1] = 0
        j+=1
    i+=1



