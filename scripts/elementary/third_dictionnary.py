car = {'brand': 'Ford', 'Model': 'Mustang', 'year': 1965, 'color': ['red', 'blue']}

print(car['brand'])

print(car.get("city", "je n'ai pas"))

car['year'] = 1964
car['city'] = "Tehran"

car.update({'brand': 'chevrolet', 'Model': 'Corvet', 'year': 1963, 'color': ['red', 'blue'], 'city': "PARIS"})
print(car)

del car['year']
car.pop('brand')
print(car)

print(len(car))

print(car.keys())
print(car.values())
print(car.items())

for key in car.keys():
    print(key)

for key,value in car.items():
    print(key, '------------', value)