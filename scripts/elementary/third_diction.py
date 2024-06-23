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

# write a function that take one of the key's of a dictionnary and return the coresponding value 
def dec_f(word, intro_text = "Hi "):
    #return "car_dictio = " + car_diction[word]    
    return f'{intro_text + car_diction[word]}'
    
print(dec_f('name'))