list = raw_input().split()
n = len(list)
for i in range(n):
    list[i]=int(list[i])
k = list[1]
matrix = [[0]*k for i in range(k)]
i = 1
j = 1
# while i<=k:
#     while j<=i:
#         if i%j != 0:
#             matrix[i-1][j-1] = 1
#         else:
#             matrix[i - 1][j - 1] = 0
#         j+=1
#     i+=12
for i in range(k):
    for j in range(k):
        if i>j:
            if (i+1) % (j+1) != 0:
                matrix[i][j] = 1
            else:
                matrix[i][j] = 0
        else:
            matrix[i][j] = 1
# print matrix
# for i in range(k):
#     matrix[i][i]=1
# list1 = [0]*k
# for i in range(k):
#     list1[i] = sum(matrix[i])+k-i+1
n = list[0]
if n == 1:
    print 1
# if n == 2
m = k
while m>0:
