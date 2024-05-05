l1 = [2, 3, 4, 2, 3, 23]
print(type(l1))
print(l1)
print()


# lists methods
# append()
fruits = ['apple', 'banana', 'cherry']
print(fruits)
print()

fruits.append("orange")
print(fruits)
print()
a = ["apple", "banana", "cherry"]
b = ["Ford", "BMW", "Volvo"]
a.append(b)
print(a)

# clear()
fruits = ['apple', 'banana', 'cherry', 'orange']
fruits.clear()
print(fruits)

#copy()
fruits = ['apple', 'banana', 'cherry', 'orange']
x=fruits.copy()
y=x
print(x)
print(y)

# count()

fruits = ['apple', 'banana', 'cherry']
x = fruits.count('cherry')
print(x)

points = [1, 3, 54, 5, 3, 4, 1]
print(points.count(1))
# extend()
cars=['ford', 'bmw', 'volvo']
fruits.extend(cars)
print(fruits)

fruit = ['apple', 'banana', 'cherry']
points = (1,3,4,5)
fruit.extend(points)
print(fruit)

# index()
fruits = ['apple', 'banana', 'cherry']
x = fruits.index('cherry')
print(x)

fruits = [4,3,54,32,3]
print(fruits.index(54))
print(fruits.index(32))

# insert()

fruits = ['apple', 'banana', 'cherry']
fruits.insert(1, "orange")
print(fruits)

#pop()
fruits = ['apple', 'banana', 'cherry']
fruits.pop()

fruits.pop(1)
print(fruits)

#remove()
fruits = ['apple', 'banana', 'cherry']

fruits.remove('banana')
print(fruits)
# reverse()
fruits = ['apple', 'banana', 'cherry']
fruits.reverse()
print(fruits)

cars = ['Ford', 'BMW', 'Volvo']
cars.sort()
print(cars)
cars.sort(reverse=True)
print(cars)
print()



def myFunc(e):
  return len(e)

cars = ['Ford', 'Mitsubishi', 'BMW', 'VW']

cars.sort(key=myFunc)
print(cars)




# Python program to interchange first and last elements in a list
def swaplist(newlist):
  size = len(newlist)
  temp = newlist[0]
  newlist[0] = newlist[-1]
  newlist[-1] = temp
  return newlist
print(swaplist([12, 35, 9, 56, 24]))

#2: The last element of the list can be referred as list[-1]. Therefore, we can simply swap list[0] with list[-1].

def swap(nl):
  nl[0],nl[-1] = nl[-1], nl[0]
  return nl

print(swap([12, 35, 9, 56, 24]))

#3: Swap the first and last element is using tuple variable. Store the first and last element as a pair in a tuple variable, say get, and unpack those elements with first and last element in that list. Now, the First and last values in that list are swapped.
def swapi(list):
  get = list[-1],list[0]
  list[0],list[-1] = get
  return list

print(swapi([12, 35, 9, 56, 24]))
#4: Using * operand.
#This operand proposes a change to iterable unpacking syntax, allowing to specify a “catch-all” name which will be assigned a list of all items not assigned to a “regular” name.

list=[1,2,3,4]
a, *b, c = list
print(a)
print(b)
print(c)

def swapl(list):
  start, *middle, end = list
  list = [end, *middle, start]
  return list
print(swapl([12, 35, 9, 56, 24]))
#5: Swap the first and last elements is to use the inbuilt function list.pop(). Pop the first element and store it in a variable. Similarly, pop the last element and store it in another variable. Now insert the two popped element at each other’s original position.
def swapop(list):
  first = list.pop(0)
  last = list.pop(-1)
  list.insert(0,last)
  list.append(first)
  return list
print(swapop([12, 35, 9, 56, 24]))

#6: Using slicing
'''In this approach, we first check if the list has at least 2 elements.
If the list has at least 2 elements, we swap the first and last elements using slicing by assigning the value of the last element to the first element and the value of the first element to the last element.
We then slice the list from the second element to the second-to-last element and concatenate it with a list containing the first element and the last element in their new positions.
'''
list=[12, 35, 9, 56, 24]
if len(list)>=2:
    list = list[-1:] + list[1:-1] + list[:1]
    print(list)