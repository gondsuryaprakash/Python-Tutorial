
# just like Arrow function in the
f=lambda a:a*a
res=f(5)
print(res)
# lambda is use for the only one expression of code

sum1=lambda a,b:a+b
print(sum1(5,6))
#  Use of lambda function
nums=[1,2,3,4,6,6,7]
evens=list(filter(lambda x:x%2==0,nums))
print(evens)
