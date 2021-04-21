'''
Author: your name
Date: 2021-04-20 21:39:09
LastEditTime: 2021-04-21 19:51:43
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /leetcode/103.二叉树的锯齿形层序遍历.py
'''
#
# @lc app=leetcode.cn id=103 lang=python3
#
# [103] 二叉树的锯齿形层序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        nums=[]
        tree_queue=[]
        tree_queue.append(root)
        left=True
        while len(tree_queue)!=0:
            temp=[]
            size=len(tree_queue)
            for i in range(size):
                current_node=tree_queue.pop()
                if left:
                    temp.append(current_node.val)
                else:
                    temp.insert(0,current_node.val)
                if current_node.left:
                    tree_queue.insert(0,current_node.left)
                if current_node.right:
                    tree_queue.insert(0,current_node.right)
            left= not left
            nums.append(temp)
        return nums
                
# @lc code=end

