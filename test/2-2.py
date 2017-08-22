k = int(raw_input())
t = int(raw_input())
nums = [1,2,3,4,5,6,7,8,9]
if k>t:
    print False
else:
    dp = [1]+[0]*t
    for i in range(len(dp)):
        for n in nums:
            if n>i:
                break
            dp[i] += dp[i-n]
    print dp[t]