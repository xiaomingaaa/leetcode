'''
Author: your name
Date: 2021-04-21 19:57:04
LastEditTime: 2021-04-21 20:01:07
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
        temp=ListNode()
        temp.next=head
        if not head:
            return head
        while head:
            temp=head.next.next
            
            head.next.next=head.next
# @lc code=end

