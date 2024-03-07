# https://leetcode.com/problems/word-break/

class Solution:
    def __init__(self):
        self.memo = {}

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        if s in self.memo:
            return self.memo[s]

        if not s :
            return True

        for word in wordDict:
            n = len(word)
            if s[:n] == word:
                if self.wordBreak(s[n:], wordDict):
                    self.memo[s]=True
                    return True
        self.memo[s]=False
        return self.memo[s]
