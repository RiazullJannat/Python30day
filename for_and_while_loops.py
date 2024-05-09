fruits = ['apple', 'banana', 'cherry']
for i in fruits:
    print(i)
for x in "banana":
    print(x)

for x in fruits:
    print(x)
    if x == 'banana':
        break
print()

for i in fruits:
    if i == 'banana':
        break
    print(i)
print()
for x in fruits:
    if x == 'banana':
        continue
    print(x)
for x in range(6):
    print(x)
print()

for x in range(2,6):
    print(x)
print()
for x in range(2,30,3):
    print(x)
print()
for x in range(6):
    print(x)
else:
    print('Finally finished!')

print()
for x in range(6):
    if x == 3: break
    print(x)
else:
    print('Finally finished')
# Nested loops
adj = ['red', 'big', 'testy']
fruits = ['apple', 'banana', 'cherry']
for x in adj:
    for y in fruits:
        print(x,y)

for x in [0, 1, 2]:
    pass
# While loop
i = 0
while (i<10):
    print(i)
    i +=1

#while True:
#   print("While loop in not finishing.......")

while True:
    #num=int(input("Enter your number: "))
    num = 0
    print(num)
    if num == 0:
        break
print('Program has finished executing.....')

i = 1
while i<6:
    print(i)
    if i == 3:
        break
    i +=1
i = 0
while i<6:
    i += 1
    if i == 3:
        continue
    print(i)

i = 1
while i < 6:
    print(i)
    i +=1
else:
    print('i is no longer less than 6')

