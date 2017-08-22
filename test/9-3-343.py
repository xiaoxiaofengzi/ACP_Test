class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        l = [-1]*(n+1)
        l[1] = 1
        i=2
        j=1
        while i<=n:
            while j<=i-1:
                l[i] = max(l[i],max(j*(i-j),j*l[i-j]))
                j+=1
            j=1
            i+=1
        return l[n]