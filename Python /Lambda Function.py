# #
# # just like Arrow function in the
# f=lambda a:a*a
# res=f(5)
# print(res)
# # lambda is use for the only one expression of code
#
# sum1=lambda a,b:a+b
# print(sum1(5,6))
# #  Use of lambda function
# nums=[1,2,3,4,6,6,7]
# evens=list(filter(lambda x:x%2==0,nums))
# print(evens)

# stats={1:10,2:10}
# b=max(stats.keys())
# print(b)
# a=max(stats, key=stats.get)
# print(a)
# a=[1,2,3,4]
# res=filter(lambda x:x>2 and x<5,a)
# print(list(res))

# def fact(n):
#     if n==0 or n==1:
#         return 1
#     return n*fact(n-1)
# a=fact(5)
# print(
#     a
# )
a=set()
a.add(5)
a.add(2)
a.add(1)
a.add(3)
a.add(4)
a.add(6)
print(a)

import random
c=list(a)
b=c[random.randrange(0,len(c))]
print(b)
