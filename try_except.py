# try block
try:
    print(x)
except:
    print("An exception occurred.")


try:
    print(x)
except NameError:
    print("Variable x is not difined.")
except:
    print("Something else went wrong.")


try:
    print("Hello")
except:
    print("something went wrong.")
else:
    print("Nothing went wrong.")

try:
    print("Hello")
except:
    print("Something went wrong.")
finally:
    print('The try except is finished.')

# rise
'''x = int(input("Enter your number:"))
if x < 0:
    raise Exception("Sorry, no numbers below zero.")'''

'''x = 'Hello'
if not type(x) is int:
    raise TypeError("Only integers are allowed.")'''


try:
    print(x)
except Exception as e:
    print('Some error occurred: ', e)
