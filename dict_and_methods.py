dict1 = {}
print(dict1,type(dict1))

# methods
# clear()
car = { 'brand': "Ford",
        'model': 'Mustang',
        'year': 1964}
print(car)

car.clear()
print(car)
# copy()
car = {'brand':'Ford', "model":'Mustang',"year":1964}

x = car.copy()
print(x)

# fromkeys()
x = {'key1', 'key2', 'key3'}
y = 0
thisdict = dict.fromkeys(x,y)
print(thisdict)

x = {'key1','key2', 'key3'}
thisdict = dict.fromkeys(x)
print(thisdict)

#get()
car = {'brand':'Ford', 'model':'Mustang', 'year':1964}
x = car.get('model')
print(x)
print(car.get('brand'))
print(car.get('price', 150000))

# items()
car = { 'brand':'Ford', 'model':'Mustang', 'year':1964}

x = car.items()
print(x)

car["year"] = 2018
print(car)
# keys()
car = {'brand':"ford", "model":"Mustang","Year":1964}
x = car.keys()
print(x)
print(car.keys())

car = {'brand':'Ford', 'model':'mustang','year':1964}
car['color'] = 'White'
print(car.keys())
print(car.values())

# pop()
car = {'brand':'ford', 'model':'mustang','year':1964}
car.pop('model')
print(car)
# popitem()

car = {'brand':'ford', 'model':'mustang','year':1964}
car.popitem()
print(car)
print()

#setdefault()
car={'brand':'ford', 'model':'mustang', 'year':1964}
x = car.setdefault('model','bronco')
print(x)
print(car)
# update()
car.update({'color':'white'})
print(car)
print(car.values())
