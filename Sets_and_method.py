a = { 3, 5, 3, 4, 6, 76}
print(a)
print()

# add()
fruits = {"apple", "banana", "cherry"}
fruits.add('orange')
print(fruits)
fruits.add("apple")
print(fruits)
print()
# clear()
fruits ={'apple', 'banana', 'cherry'}

fruits.clear()
print(fruits)
# copy()
fruits = {'apple', 'banana', 'cherry', 'golap'}
x = fruits.copy()
print(x)

# difference() -
x = {'apple', 'banana', 'cherry'}
y = {'google', 'microsoft', 'apple'}
z = x.difference(y)
print(z)
b = y.difference(x)
print(b)
# use - as a shortcut instead of difference()
a = {'apple', 'banana', 'cherry'}
b = {'google', 'microsoft', 'apple'}
my_set = a - b
my_set2 = b - a
print(my_set)
print(my_set2)

a = {'apple', 'banana', 'cherry'}
b = {'google', 'linux','mac'}
c = {'cherry', 'micra', 'bluebird'}

myset3= b.difference(a,c)
print(myset3)

a = {'apple', 'banana', 'cherry'}
b = {'google', 'microsoft', 'apple'}
c = {'cherry', 'mlicra', 'bluebird'}
myset = a - b - c
print(myset)
# difference_update() -=
x = {'apple', 'banana', 'cherry'}
y = {'google', 'microsoft', 'apple'}

x.difference_update(y)
print(x)

a = {'apple', 'banana', 'cherry'}
b = {'google', 'linux', 'apple'}

a -= b
print(a)
a = {"apple", "banana", "cherry"}
b = {"google", "linux", "apple"}
c = {"cherry", "micra", "bluebird"}

a.difference_update(b,c)
print(a)
print()

a = {'apple', 'banana', 'cherry'}
b = {'google', 'linux', 'mac'}
c = {'cherry', 'micra', 'bluebird'}
a -= b | c
print(a)


# discard()
fruits = {'apple', 'banana', 'cherry'}
fruits.discard('banana')
print()

print(fruits)


fruits = {'apple', 'banana', 'cherry'}
fruits.discard('linux')
print(fruits)

# intersection() &
x = {"apple", "banana", "cherry"}
y = {"google", "linux", "apple"}

z = a.intersection(y)
print()
print(z)
print()

x = {'apple', 'banana', 'cherry'}
y = {'google', 'linux', 'apple'}
z = x & y
print(z)


x = {'a', 'b', 'c'}
y = {'c', 'd', 'e'}
z = {'f', 'g', 'c'}
result = x.intersection(y,z)
print(result)
print(x)
# intersection_update() &=
x = {'apple', 'banana', 'cherry'}
y = {'google', 'linux', 'apple'}
x.intersection_update(y)
print(x)

print()
x = {'apple', 'banana', 'cherry'}
y = {'google', 'linux', 'apple'}
x &= y
print(x)
print(y)

x = {'a', 'b', 'c'}
y = {'c', 'd', 'e'}
z = {'f', 'g', 'c'}

x.intersection_update(y,z)
print(x)

x = {'a', 'b', 'c'}
y = {'c','d', 'e'}
z = {'f', 'g', 'c'}
x &= y | z
print(x)

# isdisjoint()
x = {"apple", "banana", "cherry"}
y = {"google", "linux", "facebook"}
z = x.isdisjoint(y)
print(z)

# issubset() <=
x = {'a', 'b', 'c'}
y = {'f', 'e', 'd', 'c', 'b', 'a'}
z = x.issubset(y)
print(z)

# issuperset() >=
x = {'f', 'e', 'd', 'c', 'b', 'a'}
y = {'a', 'b', 'c'}
z = x.issuperset(y)
print(z)
# >
print(y.issuperset(x))

# pop() remove randomly every time.
a = {'apple', 'banana', 'cherry'}
a.pop()
print(a)

# remove()
fruits = {'apple', 'banana', 'cherry'}
fruits.remove('apple')
print()
print(fruits)

# symmetric_difference() ^
x = {'apple', 'banana', 'cherry'}
y = {'google', 'linux', 'apple'}

z = x.symmetric_difference(y)
print(z)

h = x ^ y
print(h)
# symmetric_difference_update() ^=
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
#x.symmetric_difference_update(y)
x ^= y
print(x)

# Union() |
x = {'apple', 'banana', 'cherry'}
y = {'google', 'linux', 'apple'}

z = x.union(y)
print(z)
h = x | y
print(h)

x = {"a", "b", "c"}
y = {"f", "d", "a"}
z = {"c", "d", "e"}
result = x.union(y,z)
print(result)

x = {"a", "b", "c"}
y = {"c", "d", "e"}
z = {"f", "g", "c"}

result = x | y | z

print(result)

# update() |=
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.update(y)

print(x)

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x |= y

print(x)