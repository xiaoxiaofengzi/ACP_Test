if x in l:
    print(-1)
else:




while 1:     
try:         n,l=[int(c) for c in raw_input().strip().split()]         a=[int(c) for c in raw_input().strip().split()]     except:         break     a.sort()     b=max(a[0],l-a[-1])     for k in range(n-1):         s=(a[k+1]-a[k])/2.0         b=s if s>b else b     print("%.2f"%b)