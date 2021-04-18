'''
Author: your name
Date: 2021-04-18 14:07:10
LastEditTime: 2021-04-18 15:20:47
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /leetcode/26.删除有序数组中的重复项.py
'''
#
# @lc app=leetcode.cn id=26 lang=python3
#
# [26] 删除有序数组中的重复项
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        slow=1
        fast=1
        while fast<len(nums):
            if nums[fast]!=nums[fast-1]:
                ### 元素不连续，当前slow元素赋值为fast元素，slow，fast都后移
                nums[slow]=nums[fast]
                slow+=1
            ### 存在连续的元素，快指针后移，慢指针不懂
            fast+=1
        return slow
# @lc code=end

