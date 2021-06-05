'''
Author: your name
Date: 2021-06-05 19:20:58
LastEditTime: 2021-06-05 19:33:41
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \leetcode\83.删除排序链表中的重复元素.py
'''
#
# @lc app=leetcode.cn id=83 lang=python3
#
# [83] 删除排序链表中的重复元素
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        pre=head
        cur=head.next
        while cur:
            if cur.val!=pre.val:
                pre=pre.next
                cur=cur.next
            else:
                pre.next=cur.next
                cur=cur.next
        return head
            
# @lc code=end

