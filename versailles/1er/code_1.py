def days_to_hours(n):
    if n > 0:
        return  f" {n}  days is {n * 24}  hours "
    elif n == 0:
        return "enter a non zero value"


def validate_and_execute():
    if n.isdigit():
        n_entered = int(n)
        print(days_to_hours(n_entered))
    else:
        print("Dont ruine my stuf")

n = input("Enter a number please\n")
validate_and_execute()