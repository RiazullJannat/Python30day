name = 'RJannat'
print(name)

#string slicing
print(name[0:3]) #start from 0 and go all way till 2 (3-1)
print(name[1:4]) #start from 0 and go all way till 3 (4-1)

srting='riazullJannat'
print(srting[:3])
print(srting[1:5:2])
print(srting[-1:-12:-2])
print(srting[::-1])


a='thinktank'
print(a[5:5])

b='follow'
print(b[3:8])

c='medium'
print(c[-4:4])

d='pythonista'
print(d[6:2:-1])

e='program'
print(e[-6:-1:2])

#f='coder'
#print(f[::0]) gives a valou error

g='doubled'
print(g[1:6][1:3])

h='question'
print(h[-1::-2])

i='subscribe'
print(i[-3:-6:2]) #blanck output

j='completed'
print(j[2:5:3])
#write a python program to calculate the length of a string.
a='tttt'
print(len(a))

#Write a python program to count the number of characters in a stirng.
n='google'
rd={}
for i in n:
    key=rd.keys()
    if i in key:
        rd[i]+=1
    else:
        rd[i]=1
print(rd)

#write a python program to get a string made of the first 2 and last 2 characters of a given string.
#if the len is less than 2, return empty string.
n='Jannat'
if len(n)<2:
    print("Empty.")
else:
    print(n[:2]+n[-2:])



#python string methods
#capitallize()
txt="hello, and welcome to my world"
x=txt.capitalize()
print(x)

t = "21 is my age."
x = t.capitalize()
print(x)

# casefold()

te='Hello, And Wellcome To My World.'
x=te.casefold()
print(x)

# center()
text = "banana"
x = text.center(20)
print(x)

text= "banana"
x = text.center(20,"O")
print(x)

# count()
text = "I love apples, apple are my favorite fruit."
x=text.count("apple")
print(x)

text="I love apples, apple are my favorite fruit."
x=text.count('apple',10,24)
print(x)

# encode()
text = "My name is rjannat."
x= text.encode()
print(x)
# endswith()
txt = "Hello, welcome to my world."
x = txt.endswith(".")
print(x)
print(txt.endswith(','))
print(txt.endswith('my world.'))

# expandtabs()
txt = 'H\te\tl\tl\to'

print(txt)
print(txt.expandtabs())
print(txt.expandtabs(2))
print(txt.expandtabs(4))
print(txt.expandtabs(10))

# find()
txt = 'Hello, welcome to my world.'
x = txt.find('welcome')
print(x)

txt = "Hello, welcome to my world."
x= txt.find('e', 5, 10)
print(x)

txt = 'Hello, wellcome to my world.'
print(txt.find('q'))
# print(txt.index('q'))

# format()
txt='For only {cost:.3f} dollars!'
print(txt.format(cost=49))

# index()
txt = "Hello, welcome to my world."
x = txt.index("welcome")
print(x)
print(txt.index('e'))
print(txt.index('e', 5,10))


# isalnum()
txt = 'Company12'
x = txt.isalnum()
print(x)

txt = "company 12"
print(txt.isalnum())

# isalpha()

txt = "companyX"

x = txt.isalpha()
print(x)

txt = 'company10'
print(txt.isalpha())
# isascii()
txt = 'company123'
x = txt.isascii()
print(x)
