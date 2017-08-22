class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        n = len(nums)
        val = 1
        i = 0
        j = 0
        temp = 0
        while i < n:
            if nums[i] != val:
                temp = nums[i]
                nums[i] = nums[j]
                nums[j] = temp
                j += 1
                i += 1
            else:
                i += 1
        return i



