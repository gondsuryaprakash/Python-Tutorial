list1=[7,5,6,3,8,5,3,5]
tuple1=((3,8),(2,9),(1,10),(4,7))
d1={3:"e",2:"a",1:"c",7:"b"}
# Sort List
print(sorted(list1,reverse=True))
#Sort Tupple
print(sorted(tuple1))
# Sort the only key
print(sorted(d1))
# sort the value
print(sorted(d1.values()))
#
print(sorted(d1.items()))
# sort the dict on the basis of the key
print(sorted(d1.items(),key=lambda x:x[1]))
a=[[10,20],[30,200],[400,50],[30,20]]
print(sorted(a,key=lambda x:x[0]-x[1]))