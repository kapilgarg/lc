# https://leetcode.com/problems/house-robber-iii/
from typing import Optional


# Definition for a binary tree node.
# This is a bottom up approach. We start from leaf node. When we are robbing leaf node, since there is no node prior to leaf node,
# robbed value r1 (immediately before leaf node) is 0 and r2(one node before leaf node) is 0
# So the max amount bt robbing leaf node will be
# 1. rob leaf node + r1
# 2. skip leaf node => r2
# from here we return a tuple (current_node_val+r1, r2)
# at any node going up, the max rob value would be 1) either rob current node + r2 of both chile node
# 2) skip current node and sum of max of r1 and r2 for both the child nodes.
# https://leetcode.com/problems/house-robber-iii/solutions/376297/python3-dynamic-programming-depth-first-search/


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            if not root:
                return 0, 0
            left = dfs(root.left)
            right = dfs(root.right)
            return root.val + left[1] + right[1], max(left[0], left[1]) + max(right[0], right[1])

        return max(dfs(root))
