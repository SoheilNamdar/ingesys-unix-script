# Enter two numbers

n1 = int(input("first: "))
print(n1)

n2 = int(input("second: "))
print(n2)

#enter regular operations
operation = input("operation: ")

if operation == "+":
    n = n1 + n2
elif operation == "-":
    n = n1 - n2
elif operation == "*":
    n = n1 * n2
elif operation == '/':
    n = n1 / n2
else:
    print("ca va pas")
    
print(n)
