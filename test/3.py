import math
def AA():
    n = int(raw_input())
    if n % 2 == 0 or n % 5 == 0 or n < 0 or n > 10000:
        print 0
    i = 1
    while i >= 0:
        if sumNum(i) % n == 0:
            break
        else:
            i += 1
    print i

def sumNum(m):
    i = 0
    sum = 0

    while i < m:
        sum += math.pow(10, i)
        i += 1
    return sum

AA()