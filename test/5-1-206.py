import sys
exp = str(sys.stdin.readline().strip())
m=len(exp)
nums = []
stack=['#']
stackNum=[]
i=0
k=-1
while i<m:
    while k<m:
        e=exp[i]
        f=exp[k]
        if e.isdigit():
            stackNum.append(int(e))
            i+=1
        else:
            k=i
            if f.isdigit():
                stackNum.append(int(e))
                k += 1
                i += 2
        elif e=='+':
        b=stackNum.pop()
        op=stack.pop()
        stackNum.append(stackNum[0]+b)
    elif e=='-':
        b = stackNum.pop()
        a = stackNum.pop()
        op = stack.pop()
        stackNum.append(a - b)
    elif e=='*':
        b = stackNum.pop()
        a = stackNum.pop()
        op = stack.pop()
        stackNum.append(a * b)
    else:
        stack.pop()
        i+=1
print(stackNum[0])