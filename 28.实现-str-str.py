'''
Author: your name
Date: 2021-04-26 16:19:58
LastEditTime: 2021-04-26 16:28:46
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /leetcode/28.实现-str-str.py
'''
#
# @lc app=leetcode.cn id=28 lang=python3
#
# [28] 实现 strStr()
#
# @lc code=start
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        n=len(needle)
        for i in range(len(haystack)-n+1):
            if haystack[i:i+n]==needle:
                return i
        return -1
# @lc code=end

