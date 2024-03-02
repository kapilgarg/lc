# https://leetcode.com/problems/house-robber-iii/description/
class Solution:
    def rob(self, nums: List[int]) -> int:
        def _rob(nums):
            r1 = r2 = 0
            for n in nums:
                money = max(r1 + n, r2)
                r1 = r2
                r2 = money
            return r2

        return max(nums[0], _rob(nums[:-1]), _rob(nums[1:]))
