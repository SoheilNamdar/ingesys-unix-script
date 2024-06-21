car_diction = {'name' : 'ford', 'year' : 1965, 'city': 'Hoston'}

#print value of 'name'
car_diction['name']

#print all the items
print(car_diction.items())

#print all the keys
print(car_diction.keys())

#print all the keys by a for loop
for key in car_diction.keys():
    print(key)

##print keys values by a for loop in a 'key ----- value' format
for key,value in car_diction.items():
    print(key, '------', value)