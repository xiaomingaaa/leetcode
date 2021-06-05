'''
Author: your name
Date: 2021-06-05 11:40:30
LastEditTime: 2021-06-05 13:30:21
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \leetcode\80.删除有序数组中的重复项-ii.py
'''
#
# @lc app=leetcode.cn id=80 lang=python3
#
# [80] 删除有序数组中的重复项 II
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n=len(nums)
        if n<=2:
            return len(nums)
        slow=2
        fast=2
        for i in range(2, n):
            if nums[slow-2]!=nums[fast]:
                nums[slow]=nums[fast]
                slow+=1
            fast+=1
        return slow
        
# @lc code=end

