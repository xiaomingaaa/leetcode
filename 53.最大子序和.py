'''
Author: your name
Date: 2021-04-22 17:01:11
LastEditTime: 2021-04-24 20:56:22
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /leetcode/53.最大子序和.py
'''
#
# @lc app=leetcode.cn id=53 lang=python3
#
# [53] 最大子序和
#

# @lc code=start
# class Solution:
#     def maxSubArray(self, nums: List[int]) -> int:
#         dp=[0]*len(nums)
#         dp[0]=nums[0]
#         for i in range(1,len(nums)):
#             dp[i]=max(dp[i-1]+nums[i], nums[i])
        
#         return max(dp)

#     def maxSubArray_1(self, nums: List[int]) -> int:
#         current_max=nums[0]
#         for i in range(len(nums)):
#             for j in range(i+1,len(nums)+1):
#                 if current_max<sum(nums[i:j]):
#                     current_max=sum(nums[i:j])
#         return current_max

# a='HELLO'
# b=[1,2]
# print('{}'.format(a and b))
# print('{}'.format(a or b))

# l=[-2,4]
# m=map(lambda x:x*2,l)
# print(m)
def permute(nums):
        n=len(nums)
        if n<=1:
            return [nums]
        elif n==2:
            return [[nums[0],nums[1]],[nums[1],nums[0]]]
        kk=[]
        for i in range(n):
            nlst=nums[0:i]+nums[i+1:] 
            c=permute(nlst)
            ss=[]
            for j in c:
                w=[nums[i]]
                w.extend(j)
                ss.append(w)
            #kk.extend(ss)
        return kk

def judge_seq(l):
    for j in range(1,len(l)):
        if abs(l[j]-l[j-1])>2:
            return False
    return True

n=int(input())
tempList=[i for i in range(1,n)]

# for item in list(perms(tempList)):
#     if item[0]==1 or item[0]==2:
#         t=judge_seq(item)
#         if t:
#             count=(count+1)%998244353
# print(count) 

# n,k=[int(z) for z in input().split(' ')]
# ms=[int(z) for z in input().split(' ')]
# i=0
# j=k
# ans=[i,j]
# max_value=0
# while j<=n:
#     temp=sum(ms[i:j])
#     if temp>max_value:
#         max_value=temp
#         ans=[i,j]
#     j+=1
#     i+=1
# print(ans[0]+k//2+1)

n,k=[int(z) for z in input().split(' ')]
nums=[int(z) for z in input().split(' ')]
i = 0
for j in range(1, len(nums) - k + 1):
    count = 0
    while count < k and nums[j + count] == nums[i + count]:
        count += 1

    if nums[j + count] > nums[i + count]:
        i = j
print(i+k//2+1)

# @lc code=end

