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
            memo = [-1]*(c+1)
            j=0
            i=1
            k=c
            while j<=c:
                if j>=w[0]:
                    memo[j] = v[0]
                else:
                    memo[j] = 0
                j+=1
            while i<n:
                while k>=w[i]:
                    memo[j] = max(memo[j],v[i]+memo[j-w[i]])
                    k-=1
                i+=1
            return memo[c]