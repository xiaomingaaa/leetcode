'''
Author: your name
Date: 2021-04-20 21:04:55
LastEditTime: 2021-04-20 21:38:02
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /leetcode/102.二叉树的层序遍历.py
'''
#
# @lc app=leetcode.cn id=102 lang=python3
#
# [102] 二叉树的层序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        tree_queue=[]
        nums=[]
        tree_queue.insert(0, root)
        while len(tree_queue)!=0:
            size=len(tree_queue)
            temp=[]
            for i in range(size):
                current_node=tree_queue.pop()
                temp.append(current_node.val)
                if current_node.left:
                    tree_queue.insert(0, current_node.left)
                if current_node.right:
                    tree_queue.insert(0, current_node.right)
            nums.append(temp)
        return nums
        
# @lc code=end

