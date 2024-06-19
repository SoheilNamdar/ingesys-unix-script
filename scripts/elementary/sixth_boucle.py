numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
items = ['red', 'blue', 'green']
i = 0

for number in numbers:
    i += number
print(i)

print('-----///------')
for number in numbers:
    if number == 6:
        break
    print(number)

print('-----///------')
for number in numbers:
    for item in items:
        print(number, item)

print('-----///------')
for ii in range(10):
    print(ii)

print('-----///------')
for ii in range(1,10):
    print(ii)

print('-----///------')
x = 2
for ii in range(3):
    x = x*x
    print(x) 

print('-----///------') 
x = 5 
while x < 60:
    print(x)
    x +=5