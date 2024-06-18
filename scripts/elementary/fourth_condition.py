condition = False

if condition:
    print('True')
else:
    print('False')

print('---*********---') 

x = 20
if x == 20:
    print("c'est vrai")
else:
    print("c'est faux")

print('---*********---') 

if x <= 20:
    print('minuscule')
elif 20 < x < 40:
    print('moyen')
else:
    print('grand')

print('---*********---') 

x = 256
y = 256
print(x is y)
print('---*********---') 
print(id(x))
print(id(y))
print('---*********---') 
print(x is y)
print('---*********---') 
x = y
print(x == y)