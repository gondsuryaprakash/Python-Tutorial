# number=[1,2,3,4,5,5]
# # print(names[:])
# # big=names[0]
# # for i in names:
# #     if names[i]>big:
# #         big=names[i]
# # print(big)
# # '''2D List'''
# '''Append'''
# number.append(30)
# print(number)
# '''Insert'''
# number.insert(2,4)
# print(number)
# '''remove'''
# number.remove(5)
# number.remove(5)
# print(number)
# '''pop'''
# number.pop()
# print(number)
# '''index'''
# # print(number.index(6))
# '''in'''
# print(50 in number)
#
# print(number)
# '''count'''
# print('count of 4: '+str(number.count(4)))
# '''sort'''
# number.sort()
# print(number)
# number.reverse()
# print(number)
#
# '''copy'''
# number2=number.copy()
# print(number2)
#
#
# '''clear'''
# number.clear()
finalresul=[]
number=[1,2,2,334,12,12,5]
print(15 in number)
#
for numbers in number:
    if numbers not in finalresul:
        finalresul.append(numbers)

print(finalresul)