# def getCelebraty(m,n):
#     stack=[]
#     for i in range(n):
#         stack[i].insert(0,i)
#
#     for i in range(n):
#         for j in range(n):
#             x1=stack.pop(0)
#             x2=stack.pop(0)
#             if m[x1][x2]==0 and m[x2][x1]==1:
#                 stack.insert(x1,0)
#             elif m[x1][x2]==1 and m[x2][x1]==0:
#                 stack.insert(x2, 0)
#             else:
#                 stack.pop(0)
#                 stack.pop(0)
#     if len(stack)>0:
#         return stack[0]
#     else:
#         return -1
#
#
# t=int(input())
# for i in range(t):
#
#








