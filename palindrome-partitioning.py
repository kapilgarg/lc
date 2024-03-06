# https://leetcode.com/problems/palindrome-partitioning/
# This problem can be solved using dp since this can be broken down in sub problems. 
# First we split at first substring  which is a pelindrom and then for the remaining string, repeat the process.
class Solution:
    def _partition(self,s):
        if not s:
            return [[]]
        N = len(s)
        ans=[]
        
        for i in range(1, N+1):
            l = s[:i]
            if s[:i] != s[:i][::-1]:
                continue
            if not tuple(s[i:]) in self.memo:
                self.memo[tuple(s[i:])] = self._partition(s[i:])
            r = self.memo[tuple(s[i:])]

            for e in r:
                ans.append([l]+e)
        return ans
    def partition(self, s: str) -> List[List[str]]:
        self.memo={}
        return self._partition(s)
