print('####################################################################################')
def decimal(n):
    # entier à décomposer
    #n = 123
    # initialisation
    r = n
    chiffres = []
    # détermination des chiffres
    while r != 0:
        chiffres.append(r % 10)
        r = r // 10
        chiffres.reverse()
    return chiffres

print(decimal(144))

print(decimal(123))

print(bin(123))
print(hex(123))