nums = [3,2,2,2,3]
n = len(nums)
val = 3
i = 0
j = 0
temp = 0
while i < n:
    if nums[i] != val:
        temp = nums[i]
        nums[i] = nums[j]
        nums[j] = temp
        j += 1
        i+=1
    else:
        i += 1
print j
print nums