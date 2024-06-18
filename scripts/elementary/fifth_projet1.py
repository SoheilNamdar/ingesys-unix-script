num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Enter the operation: ")

print(num1, num2, operation)

if operation == "+":
    num = num1 + num2
elif operation == "-":
    num = num1 - num2
elif operation == "*":
    num = num1 * num2 
elif operation == "/":
    num = num1 / num2 
else:
    print("not a good signe.") 

print(num)