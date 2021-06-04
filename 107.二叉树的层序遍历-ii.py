'''
Author: your name
Date: 2021-05-23 11:00:32
LastEditTime: 2021-05-28 11:03:20
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \leetcode\107.二叉树的层序遍历-ii.py
'''
#
# @lc app=leetcode.cn id=107 lang=python3
#
# [107] 二叉树的层序遍历 II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        tree_queue=[]
        tree_queue.insert(0,root)
        leaf_list=[]
        while len(tree_queue)!=0:
            temp=[]
            size=len(tree_queue)
            for i in range(size):
                node=tree_queue.pop()
                temp.append(node.val)
                if node.left:
                    tree_queue.insert(0, node.left)
                if node.right:
                    tree_queue.insert(0, node.right)
            leaf_list.insert(0, temp)
        return leaf_list
        
            
# @lc code=end

