newlist = [12, 35, 9, 56, 24]
size = len(newlist)
print(size)
temp =newlist[0]
print(temp)
newlist[0] = newlist[size-1]
print(newlist[size-1])

#4: Using * operand.
#This operand proposes a change to iterable unpacking syntax, allowing to specify a “catch-all” name which will be assigned a list of all items not assigned to a “regular” name.


