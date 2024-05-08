age = int(input("Enter your age:"))
if (age>=18):
    print('Yes You can drive.')
else:
    print("NO, you can go home.")

a = 33
b = 200
if b>a:
    print("b is greater than a ")
a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")

a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")


# 1. Write a Python program to find those numbers which are divisible by 7 and multiples of 5, between 1500 and 2700 (both included).
nl =[]
for i in range(1500,2701):
    if (i % 7 == 0) and (i % 5 == 0):
        nl.append(str(i))
print(','.join(nl))
