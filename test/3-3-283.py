
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        nums = [1,0,4,6,0,4]
        k = 0
        n = len(nums)
        for i in range(n):
            if nums[i] != 0:
                nums[k] = nums[i];
                k += 1;
        while k < n:
            nums[k] =0;
            k +=1;
