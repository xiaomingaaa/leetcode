'''
Author: your name
Date: 2021-05-22 16:34:48
LastEditTime: 2021-05-22 17:39:52
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \leetcode\141.环形链表.py
'''
#
# @lc app=leetcode.cn id=141 lang=python
#
# [141] 环形链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next:
            return False
        slow = head
        fast = head.next
        while slow != fast:
            if not fast or not fast.next:
                return False
            slow = slow.next
            fast = fast.next.next
        return True


# @lc code=end
