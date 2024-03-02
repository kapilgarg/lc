from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        r1=r2=0

        for n in nums:
            moneyRobbed = max(r2, r1+n)
            r1=r2
            r2 = moneyRobbed

        return r2