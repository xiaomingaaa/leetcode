'''
Author: your name
Date: 2021-04-18 13:51:20
LastEditTime: 2021-04-18 14:05:02
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /leetcode/217.存在重复元素.py
'''
#
# @lc app=leetcode.cn id=217 lang=python3
#
# [217] 存在重复元素
#

# @lc code=start
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums)!=len(set(nums))

    def containsDuplicate_2(self, nums: List[int]) -> bool:
        num_dict=set()
        for n in nums:
            if n in num_dict:
                return True
            else:
                num_dict.add(n)
        return False

    def containsDuplicate_1(self, nums: List[int]) -> bool:
        num_dict=dict()
        for n in nums:
            if n in num_dict:
                num_dict[n]+=1
            else:
                num_dict[n]=1
            if num_dict[n]>=2:
                return True
        return False
# @lc code=end

