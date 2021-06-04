# @before-stub-for-debug-begin
from python3problem92 import *
from typing import *
# @before-stub-for-debug-end

'''
Author: your name
Date: 2021-05-28 11:04:48
LastEditTime: 2021-06-04 10:52:07
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \leetcode\92.反转链表-ii.py
'''
#
# @lc app=leetcode.cn id=92 lang=python3
#
# [92] 反转链表 II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        def reverseLinkList(head: ListNode):
            pre=None
            current=head
            while current:
                next_node=current.next
                current.next=pre
                pre=current
                current=next_node
        temp_node=ListNode(-1)
        temp_node.next=head
        pre=temp_node
        for _ in range(left-1):
            pre=pre.next
        right_node=pre
        for _ in range(right-left+1):
            right_node=right_node.next
        left_node=pre.next
        curr=right_node.next
        pre.next=None
        right_node.next=None
        reverseLinkList(left_node)
        pre.next=right_node
        left_node.next=curr
        return temp_node.next
# @lc code=end

