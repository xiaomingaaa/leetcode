#
# @lc app=leetcode.cn id=222 lang=python3
#
# [222] 完全二叉树的节点个数
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if root==None:
            return 0
        ### 深度优先遍历
        left=self.countNodes(root.left)
        right=self.countNodes(root.right)
        return left+right+1
# @lc code=end

