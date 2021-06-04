# @before-stub-for-debug-begin
from python3problem206 import *
from typing import *
# @before-stub-for-debug-end

'''
Author: your name
Date: 2021-04-21 19:57:04
LastEditTime: 2021-05-29 17:31:38
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /leetcode/206.反转链表.py
'''
#
# @lc app=leetcode.cn id=206 lang=python3
#
# [206] 反转链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        pre=None
        current=head
        while current:
            next_node=current.next
            current.next=pre
            pre=current
            current=next_node
        return pre
# @lc code=end

