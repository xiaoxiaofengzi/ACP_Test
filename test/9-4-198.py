class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n==0:
            return 0
        l = [-1]*n
        l[n-1]=nums[n-1]
        i= n-2
        while i>=0:
            j=i
            while j<n:
                if j+2<n:
                    l[i] = max(l[i],nums[j]+l[j+2])
                else:
                    l[i] = max(l[i],nums[j])
                j+=1
            i-=1
        return l[0]