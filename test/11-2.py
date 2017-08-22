a,b,c = (int(x) for x in raw_input().split(','))
p=0
if a>0 and b>0 and c>0 and a<9 and b<9 and c<9 and a != b and b!=c and c!=a:
    if a*b==10 or a*c == 10 or b*c==10 or a*b==54 or a*c == 54 or b*c==54:
        print -1
    else:
        l = max(a,b,c)
        s = min(a,b,c)
        m = a+b+c-l-s
        if a!=5 and b!=5 and c!=5 and a!=2 and b!=2 and c!=2 and a!=6 and b!=6 and c!=6 and a!=9 and b!=9 and c!=9:
            if l==3:
                print 3
            if l==4:
                print s*10+m
            if l==5:
                print s*10+l
            if l==6:
                print m*10+s
            if l==7:
                print m*10+l
            if l==8:
                print l*10+s
            if l==9:
                print l*10+m
        if (a==9 or b==9 or c==9 or a==6 or b==6 or c==6) and a!=5 and b!=5 and c!=5 and a!=2 and b!=2 and c!=2:
            if a==9 or b==9 or c==9:
                ll = sorted([a,b,c,6])
                if ll[0]==6:
                    print 79
                else:
                    print ll[1]*10+ll[2]
            else:
                ll = sorted([a, b, c, 9])
                if ll[0] == 6:
                    print 78
                if ll[2] == 7:
                    print ll[0] * 10 + 9
                if ll[2] ==8:
                    print 60+ll[0]
        if (a==5 or b==5 or c==5 or a==2 or b==2 or c==2) and a!=6 and b!=6 and c!=6 and a!=9 and b!=9 and c!=9:
            if a==5 or b==5 or c==5:
                ll = sorted([a,b,c,2])
                if ll[3] == 5:
                    print ll[0]*10+ll[1]
                if ll[2] == 5 and ll[0] == 2:
                    if ll[3]==7:
                        print 72
                    if ll[3]==8:
                        print 80+ll[1]
            else:
                ll = sorted([a,b,c,5])
                if ll[3] == 5:
                    print ll[ll[2]-1]
                if ll[2] == 5 and ll[0] == 2:
                    if ll[3]==7:
                        print 72
                    if ll[3]==8:
                        print 80+ll[1]
        else:
            if (9 in [a,b,c]) and (5 in [a,b,c]):
                p = a+b+c-9-5
                ll = sorted[p, 2, 5, 6, 9]
                if p == 1:
                    print 16
                else:
                    if p < 5:
                        print 26
                    else:
                        print 20 + p
            if (9 in [a, b, c]) and (2 in [a, b, c]):
                p = a + b + c - 9 - 2
                ll = sorted[p, 2, 5, 6, 9]
                if p == 1:
                    print 16
                else:
                    if p < 5:
                        print 26
                    else:
                        print 20 + p
            if (6 in [a, b, c]) and (5 in [a, b, c]):
                p = a + b + c - 6 - 5
                ll = sorted[p, 2, 5, 6, 9]
                if p == 1:
                    print 16
                else:
                    if p < 5:
                        print 26
                    else:
                        print 20 + p
            if (6 in [a, b, c]) and (2 in [a, b, c]):
                p = a + b + c - 6 - 2
                ll = sorted[p, 2, 5, 6, 9]
                if p == 1:
                    print 16
                else:
                    if p < 5:
                        print 26
                    else:
                        print 20 + p

else:
    print -1