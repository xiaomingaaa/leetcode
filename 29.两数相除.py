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
        ### 在这一题中，无法使用python的sys.maxsize(),这个与计算机位数有关，对于64位的系统，最大表示为2^64-1
        MAX_INT_32=2147483647
        MIN_INT_32=-2147483648
        import sys
        
        if divisor==-1 and dividend==MIN_INT_32:
            return MAX_INT_32
        sign=1
        if (dividend>0 and divisor<0) or (dividend<0 and divisor>0):
            sign=-1
        if dividend>0:
            dividend=-dividend
        if divisor>0:
            divisor=-divisor
        if dividend>divisor:
            return 0
        result=self.div(dividend,divisor)
        if sign==-1:
            result=-result
        return result
        
    def div(self,a,b):
        if a>b:
            return 0
        count=1
        tb=b
        while tb+tb>a and tb+tb<0:
            tb=tb+tb
            count=count+count
        return count+self.div(a-tb,b)
# @lc code=end

