class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        i = 0
        j = n-1
        A = (n-1)*min(height[0],height[n-1])
        while i<j:
            if height[i]<=height[j]:
                if height[i+1]>height[i]:
                    i+=1
                    A = max(A, min(height[i], height[j]) * (j - i))
                else:
                    i+=1
            if height[i]>height[j]:
                if height[j-1]>height[j]:
                    j-=1
                    A = max(A, min(height[i], height[j]) * (j - i))
                else:
                    j-=1
        return A

