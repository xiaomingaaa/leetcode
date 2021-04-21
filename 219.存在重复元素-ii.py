'''
Author: your name
Date: 2021-04-18 15:21:35
LastEditTime: 2021-04-21 19:34:19
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /leetcode/219.存在重复元素-ii.py
'''
#
# @lc app=leetcode.cn id=219 lang=python3
#
# [219] 存在重复元素 II
#

# @lc code=start
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        count_set=list()
        for i in range(len(nums)):
            if nums[i] in count_set:
                return True
            count_set.append(nums[i])
            if len(count_set)>k:
                count_set.remove(nums[i-k])
        return False
    
    
    '''
    @description: 维护一个滑动窗口，超时
    @param {*} self
    @param {List} nums
    @param {int} k
    @return {*}
    '''    
    def containsNearbyDuplicate_1(self, nums: List[int], k: int) -> bool:
        for i in range(len(nums)-k):
            if len(set(nums[i:i+k+1]))!=len(nums[i:i+k+1]):
                return True
        return False
# @lc code=end

