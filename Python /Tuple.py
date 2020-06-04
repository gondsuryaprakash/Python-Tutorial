# Creating the Tupple
Tuple1=()
print(Tuple1)

Tuple1=('Geeks','For')
print(Tuple1)

list1 = [1, 2, 4, 5, 6]
print(tuple(list1))

a='Surya is don'
print(tuple(a))

# Accessing the Tupple
Tuple1 = ("Geeks", "For", "Geeks")
a,b,c=Tuple1
print(a,b,c)
print(Tuple1[1])

# Concatanation of the tupple
Tuple1 = (0, 1, 2, 3)
Tuple2 = ('Geeks', 'For', 'Geeks')
Tuple3=Tuple1+Tuple2
print(Tuple3)

# Slicing of the Tupple
Tuple1=tuple('GEEKSFORGEEKS')
print(Tuple1[1:])
# Reversing the Tupple
print(Tuple1[::-1])

# Deletinh the Tupple
# Hence the tupple are immutable so it is not possible to delete the tupple
del Tuple1
print(Tuple1)