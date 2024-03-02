from functools import reduce
# https://leetcode.com/problems/house-robber/
# Iterate over the houses and at each house, maximize the amount that can be robbed.
# At first house, rob it.
# At 2nd house, since we can not rob consecutive houses, we pick the max of first and second.
# At 3rd house, we have two options. we can rob the 3rd house. in that case the total amount will be amount of 3rd house and amound robbed till 1st
# house. or we can rob 2nd house . which ever is max. This is tracked using two variable r1 and r2. when we are at house i, r1 will be money robbed 
# till i-2 and r2 will be robbed money till i-1.

from typing import List



class Solution:
    def rob(self, nums: List[int]) -> int:
        r1 = r2 = 0

        for n in nums:
            moneyRobbed = max(r2, r1 + n)
            r1 = r2
            r2 = moneyRobbed

        return r2


    def rob_2(self, nums: List[int]) -> int:
        return reduce(lambda a, x: (a[1], max(a[1], a[0] + x)), nums, (0, 0))[1]

