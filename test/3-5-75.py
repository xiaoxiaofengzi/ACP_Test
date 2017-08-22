class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        zero = -1;
        i = 0;
        tem = 0;
        n = len(nums);
        while i<n:
            if nums[i] == 1:
                i += 1;
            elif nums[i] ==2:
                tem = nums[i];
                nums[i] = nums[n-1];
                nums[n-1] = tem;
                n -= 1;
            else:
                zero+=1;
                tem = nums[i];
                nums[i] = nums[zero];
                nums[zero] = tem;
                i+=1;