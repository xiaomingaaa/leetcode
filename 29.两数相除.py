#
# @lc app=leetcode.cn id=29 lang=python
#
# [29] 两数相除
#

# @lc code=start
class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        import sys
        if dividend==0:
            return 0
        if divisor==1:
            return dividend
        if divisor==-1 and dividend==(-sys.maxsize-1):
            return 
        
# @lc code=end

