'''
Author: your name
Date: 2021-06-17 20:55:01
LastEditTime: 2021-06-17 21:30:15
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \leetcode\完全背包.py
'''

# def track(d, c, w):
#     x = []
#     while c > 0:                                                #因为可以重复，所以每次都需要重新寻找w
#         for i in range(len(w), 1, -1):
#             if d[i][c] != d[i - 1][c]:
#                 x.append(w[i - 1])
#                 c = c - w[i - 1]
#                 break
 
#     if d[1][c] > 0:
#         x.append(w[0])
#     return x
# 01背包问题
# target=int(input())
# C=[int(x) for x in input().split(',')]
# V=[int(x) for x in input().split(',')]
# # C = [3,2,6,7,1,4,9,5]#cost 单个物品所占容量
# # V = [6,3,5,8,3,1,6,9]#每个物品的价值
# F = [0 for i in range(0,target+1)] #初始化 元素个数为背包大小加1（target+1）
# n = len(C)

# def ZeroOneBackPack(cost,value):
#     for i in reversed(range(cost,target+1)): #逆序遍历
#         F[i] = max(F[i],F[i-cost]+value)

# for i in range(0,n):
#     ZeroOneBackPack(C[i],V[i])
# print (F[target])

nodes_time=[int(x) for x in input().split(',')]
graph=[]
line=input()
for idx, l in enumerate(line.split(';')):
    graph.append([int(x) for x in input().split(',')])
