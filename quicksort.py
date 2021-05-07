'''
Author: your name
Date: 2021-04-22 13:35:02
LastEditTime: 2021-04-22 15:36:19
LastEditors: Please set LastEditors
Description: 快速排序
FilePath: /leetcode/quicksort.py
'''
def quicksort(nums, left, right):
    if left<right:
        i=left
        j=right
        x=nums[left]
        while i<j:
            while i<j and nums[j]>=x:
                j-=1
            if i<j:
                nums[i]=nums[j]
                i+=1
            while i<j and nums[i]<x:
                i+=1
            if i<j:
                nums[j]=nums[i]
                j-=1
        nums[i]=x
        quicksort(nums,left,i-1)
        quicksort(nums,i+1,right)

a=[1,3,2,4,2]
quicksort(a,0,len(a)-1)
print(a)

        