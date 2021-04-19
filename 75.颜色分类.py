'''
Author: your name
Date: 2021-04-18 18:56:40
LastEditTime: 2021-04-19 15:20:59
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /leetcode/75.颜色分类.py
'''
#
# @lc app=leetcode.cn id=75 lang=python3
#
# [75] 颜色分类
#

# @lc code=start
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        p0=p1=0
        for i in range(n):
            if nums[i]==1:
                nums[i], nums[p1]=nums[p1], nums[i]
                p1+=1
            elif nums[i]==0:
                nums[i], nums[p0]=nums[p0], nums[i]
                if p0<p1:
                    nums[i], nums[p1]=nums[p1], nums[i]
                p0+=1
                p1+=1
        

    '''
    @description: 使用单指针两次交换元素
    @param {*} self
    @param {List} nums
    @return {*}
    '''    
    def sortColors_single(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i=0
        for j in range(len(nums)):
            if nums[j]==0:
                temp=nums[i]
                nums[i]=nums[j]
                nums[j]=temp
                i+=1
        
        for j in range(len(nums)):
            if nums[j]==1:
                temp=nums[i]
                nums[i]=nums[j]
                nums[j]=temp
                i+=1

    '''
    @description: 统计颜色数量，重写数组
    @param {*} self
    @param {List} nums
    @return {*}
    '''    
    def sortColors_1(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count_dict=dict()
        for n in nums:
            if n in count_dict:
                count_dict[n]+=1
            else:
                count_dict[n]=1
        flag=0
        count_dict=sorted(count_dict.items(), key=lambda x:x[0])
        for k,count in count_dict:
            for i in range(count):
                nums[flag]=k
                flag+=1

# @lc code=end

