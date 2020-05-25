# # a=29
# # sum=0
# # for i in str(19):
# #     sum+=int(i)**2
# # # print(sum)
# # def Sum(num):
# #     sum=0
# #     for i in str(num):
# #         sum+=int(i)**2
# #     if sum==1:
# #         return True
# #     else:
# #         return Sum(sum)
# #
# # a=Sum(19)
# # print(a)
# def palindrome(x):
#     if x<0:
#         return False
#     y=x
#     res=0
#     while y>0:
#         rem=y%10
#         res=res*10+rem
#         y=y//10
#
#     if res==x:
#         return True
#     else:
#         return False
#
# a=palindrome(-121)
# print(a)


list1=[3,2,1,]
list2=['three','two','one']
list1,list2=zip(*sorted(zip(list1,list2)))
print(list1)
print()
print(list2)