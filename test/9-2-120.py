class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        n = len(triangle)
        m = n+1
        l = []
        for i in range(m):
            l.append([10000000000000 for col in range(i)])
        l.pop(0)
        l[n-1] = triangle[n-1]
        i=n-2
        j=n-2
        while i>=0:
            while j>=0:
                l[i][j] = triangle[i][j] + min(l[i+1][j],l[i+1][j+1])
                j-=1
            j=i-1
            i-=1
        return l[0][0]
