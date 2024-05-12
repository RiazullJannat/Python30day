def sayhello(name, ending):
    print(f"Hello {name}.")
    print("Hello")
    print("Hello")
    print(f"{ending} {name}.")



sayhello('Rjannat','Thank you')


def my_function():
    print("Hello from a function.")

my_function()

def my_function1(fname):
    print(fname + "Refsnes")

my_function1("Email")
my_function1("Tobias")
my_function1("Linus")

# args
def my_function2(*kids):
    print(f"The youngest child is {kids[2]}.")

my_function2('Email', "Tobias", "Linus")

def sum_of_numbers(*numbers):
    r = 0
    for i in numbers:
        r +=i
    return r
print(sum_of_numbers(1,2,3,4))

# **kwargs

def my_function3(**kwargs):
    print(f'His last name is {kwargs["lname"]}')

my_function3(fname = 'Riaz', lname = 'Jannat')

def my_function4(**detail):
    for key, value in detail.items():
        print(f"{key} is {value}")
my_function4(name = 'rjannat', age = 21)


def my_function5(country = "Bangladesh"):
    print(f"I am from {country}")

my_function5('Madina')
my_function5()

def my_function6(food):
    for x in food:
        print(x)
fruits = ['apple', 'banana', 'cherry']

my_function6(fruits)

def my_function7(x):
    return 5 * x

print(my_function7(3))
print(my_function7(5))
print(my_function7(9))

def my_function8():
    pass

def my_function9(x, /):
    print(x)
my_function9(5)