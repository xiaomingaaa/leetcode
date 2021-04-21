'''
Author: your name
Date: 2021-04-21 20:03:10
LastEditTime: 2021-04-21 20:31:50
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /leetcode/3.无重复字符的最长子串.py
'''
#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#

# @lc code=start
class Solution:
    def is_peat(self, s):
        if len(s)!=len(set(s)):
            return True
        else:
            return False 
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)==0:
            return 0
        i=0
        j=1
        max_num=0
        while i<len(s) and j<=len(s):
            if not self.is_peat(s[i:j]):
                if max_num<len(s[i:j]):
                    max_num=len(s[i:j])
                j+=1
            else:
                i+=1
                j=i+1
        return max_num

test=Solution()
test.lengthOfLongestSubstring("pwwkew")
        
# @lc code=end

