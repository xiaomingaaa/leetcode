'''
Author: your name
Date: 2021-04-27 15:09:48
LastEditTime: 2021-04-29 20:05:48
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /leetcode/demo.py
'''

# class Node:
#     def __init__(self,val):
#         self.next=None
#         self.val=val


# def reverse_linklist(head):
#     if head == None or head.next==None:
#         return head
#     last = reverse_linklist(head.next)
#     head.next.next = head
#     head.next = None
#     return last

# a=Node(1)
# a.next=Node(2)
# a.next.next=Node(3)
# result=reverse_linklist(a)
# while result!=None:
#     print(result.val)
#     result=result.next

# T=int(input())
# result=[]
# for i in range(T):
#     N=int(input())


# x=input()
# k=int(input())

# x=[int(z) for z in x]
# def count(s):
#     t=0
#     for i in s:
#         if i==1:
#             t+=1
#     return t
# j=len(x)-1
# while j>0:
#     x[j]=x[j]+1
#     te=j
#     while x[te]==2:
#         x[te]=0
#         x[te-1]=x[te-1]+1
#         te-=1
#     if count(x)==k:
#         print(''.join([str(z) for z in x]))
#         j=0


# N=int(input())
# x=input()
# ans=0
# for i in range(len(x)):
#     for j in  range(i+1,len(x)+1):
#         cur=x[:i]+''.join(['1' if z=='0' else '0' for z in x])+x[j:]
#         ans=max(cur.count('1'),ans)
# print(ans)

# import collections
# n=int(input())
# nums=[int(z) for z in input()]

# n_count=dict(collections.Counter(nums))

# f=False
# for k,v in sorted(n_count.items(), key=lambda x:x[0]):
#     if v>1:
#         continue
#     else:
#         print(k)
#         f=True
#         break
# if not f:
#     print(-1)
    

# n,m=[int(z) for z in input().split(' ')]
# matrix=[]
# for i in range(n):
#     matrix.append([int(z) for z in input()])
# def bfs(matrix,i,j,flag=1):
#     queue=[[i,j]]
#     while queue:
#         [i,j]=queue.pop(0)
#         if 0<=i<len(matrix) and 0<=j<len(matrix[0]) and matrix[i][j]==flag:
#             matrix[i][j]=0
#             queue+=[[i+1,j],[i-1,j],[i,j-1],[i,j+1]]

# def search():
#     count=0
#     for flag in [1,2,3]:
#         for i in range(len(matrix)):
#             for j in range(len(matrix[0])):
#                 if matrix[i][j]!=flag:
#                     continue
#                 bfs(matrix,i,j,flag)
#                 count+=1
#     print(count)
# search()

# n=int(input())
# result=[]
# for i in range(n):
#     m=int(input())
#     graph=dict()
#     u,v=[int(z) for z in input().split(' ')]
#     if u not in graph:
#         graph[u]=[[u,v]]
#     else:
#         graph[u].append([u,v])


n = 5
data = [2,3,1,1,4]
dp = [0] * n
j = 0
for i in range(1, n):
    while j + data[j] < i:
        j += 1
    dp[i] = dp[j] + 1
# print(dp)
print(dp[n - 1])
