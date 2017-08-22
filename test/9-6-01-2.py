class package01:
    def package(self,w,v,c):
        '''
        :param w:list,每件物品重量
        :param v: list，价值
        :param c: 容量
        :return:
        '''
        if len(w) == len(v):
            n = len(w)
            memo = [[-1] * 2 for row in range(c+1)]
            j=0
            i=1
            k=0
            while j<=c:
                if j>=w[0]:
                    memo[0][j] = v[0]
                else:
                    memo[0][j] = 0
                j+=1
            while i<n:
                memo[i % 2][j] = memo[(i - 1) % 2][j]
                while k<=c:
                    memo[i%2][j] = max(memo[(i-1)%2][j],v[i]+memo[(i-1)%2][j-w[i]])
                    k+=1
                i+=1
            return memo[(n-1)%2][c]