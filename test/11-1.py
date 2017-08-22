#coding:utf-8
i=100
a=0
b=0
c=0
d = 0
sum = 0
while i < 1000:
    a=i//100
    b=(i%100)//10
    c=(i%100)%10
    if i == a*a*a+b*b*b+c*c*c:
        d += 1
        sum +=i
        print("第%d个水仙花数：%d"%(d,i))
    i += 1
print("水仙花数总和为：%d"%sum)