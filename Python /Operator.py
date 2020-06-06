
# Identity operator
# is
a1=3
b1=3
print(a1 is b1)

# Member Operator
# in
x='Geeksforgeeks'
y={3:'a',4:'b'}
print('G' in x)

# ternary operator
# [on_true] if [expression] else [on_false]
a,b=10,20
min=a if a<b else b
print(min)
# (if_test_false,if_test_true)[test]
print((b,a)[a<b])
print((lambda: b, lambda: a)[a < b]())


# any
# Returns true if any of the items is True.
print (any([False, False, False, False]))

# all
# Returns true if all of the items are True (or if the iterable is empty).
a=["H","a","n","n","a","h"]
print(a[::-1])