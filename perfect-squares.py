# https://leetcode.com/problems/perfect-squares/description/
class Solution:
    def numSquares(self, n: int) -> int:        
        squares = [i*i for i in range(1, int(sqrt(n))+1)]
        dp = [float('inf')]*(n+1)
        dp[:2] = [0,1]

        for i in range(2, n+1):
            for s in squares:
                if i == s:
                    dp[i]=1
                elif s<i:
                    dp[i] = min(dp[i], dp[i-s]+dp[s])
                else:
                    break
        return dp[-1]
