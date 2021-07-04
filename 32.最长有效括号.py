'''
Author: your name
Date: 2021-06-05 19:35:53
LastEditTime: 2021-06-29 11:42:59
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \leetcode\32.最长有效括号.py
'''
#
# @lc app=leetcode.cn id=32 lang=python3
#
# [32] 最长有效括号
#

# @lc code=start
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        max_len=0
        stack=[-1]
        for i in range(len(s)):
            if s[i]=='(':
                stack.append(i)
            else:
                stack.pop()
                if len(stack)==0:
                    stack.append(i)
                else:
                    max_len=max(max_len, i-stack[-1])
        return max_len

# @lc code=end