from functools import reduce
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
