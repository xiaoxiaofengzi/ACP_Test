class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        i = 0;
        n = len(numbers)-1;
        while i < n:
            if(numbers[i]+numbers[n] == target):
                m = [i+1,n+1];
                return m;
            elif (numbers[i]+numbers[n] < target):
                i+=1;
            else:
                n-=1;
        print('No results');