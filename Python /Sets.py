# Creating the set

set1=set()
print("Initial Set")
print(set1)

set1=set("Geeks For Geeks")
print(set1)

set1 = set([1, 2, 4, 4, 3, 3, 3, 6, 5])
print(set1)

set1 = set([1, 2, 'Geeks', 4, 'For', 6, 'Geeks'])
print(set1)


# Adding element to set
set1=set()
set1.add(8)
set1.add(87)
print(set1)
# using update method
# for adding two or more data adding is use
set1 = set([ 4, 5, (6, 7)])
set1.update([10, 11])
print(set1)

# Accessing in the set
