nums = [1,1,1,1,1,2]
n1 = len(nums)
i = 0
# count = 1
j = 0
# m=[]
n = []
if nums == []:
    count = 0
elif len(nums) == 1:
    count = 1
else:
    nums[j] = nums[0]
    while i < n1 - 1:
        if nums[i + 1] != nums[i]:
            s = i + 1 - j
            if s == 1:
                n.append(nums[i])
            else:
                n.append(nums[i])
                n.append(nums[i])
            j = i + 1
        i += 1
    if nums[-2] == nums[-1]:
        n.append(nums[-1])
        n.append(nums[-1])
    else:
        n.append(nums[-1])
    count = len(n)
    nums = n
print nums
print count