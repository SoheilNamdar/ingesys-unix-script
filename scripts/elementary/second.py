colors = ['red', 'blue', 'green' ]
numbers = [1, 4, 10, 23, 5, 8]

print(len(numbers))
print(colors[2])
print(numbers[1:4])

colors.append('pink')
print(colors)

colors.insert(1,'pink')
print(colors)

colors2 = ['white', 'black']
colors.extend(colors2)
print(colors)

colors.pop()
print(colors)

print('---*********---') 
numbers.sort()
print(numbers)

numbers.sort(reverse = True)
print(numbers)

sorted_colors = sorted(colors)
print(sorted_colors)

print('---*********---') 
for color in colors:
    print(color)

for color in colors:
    print(color.count('e'))

print('---*********---') 
print('pink' in colors)

print(23 in numbers)

print('---*********---') 

for index, color in enumerate(colors):
    print(index, color)

print('---*********---') 
print('.'.join(colors))

message = 'red.pink.blue.green.pink.white'
print(message.split('.'))

print('---**** Tuplet *****---') 
#Tuplet
numbs_tuplet = tuplet()

colors = ('red', 'blue', 'green', 'blue', 'blue')
print(colors.index('blue'))

print('---***** List ****---') 
#list
numbs_list = list()

colors = ['red', 'blue', 'green', 'green','blue', 'blue']
print(len(colors))
print(colors.index('blue'))

print('---**** Set *****---') 
#Set - tartib mohem nist
numbs_set = set()

colors = {'red', 'blue', 'green', 'green','blue', 'blue'}
print(len(colors))
#print(colors.index('blue')) nadarim index() aslan chon tartib va tedad mohem nist

colors_set1 = {'red', 'blue', 'green', 'green','blue', 'blue', 'white'}
colors_set2 = {'red', 'blue', 'green', 'green','black'}
print(colors_set1.union(colors_set2))
print(colors_set1.intersection(colors_set2))
print(colors_set1.difference(colors_set2))

