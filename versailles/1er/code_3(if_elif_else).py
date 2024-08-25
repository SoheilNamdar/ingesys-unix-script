def days_to_hours(number_of_days):
    if number_of_days > 0:
        return f"{number_of_days} days is : {number_of_days * 24} hours."
    elif number_of_days == 0:
        return "You enter zero, please enter a positive number"


def validate_and_execute():
    if user_input.isdigit():
        user_input_number = int(user_input)
        print(days_to_hours(user_input_number))
    else:
        print("stop enter a test and ruine my program")

user_input = input("Enter a number of days and i convert it to hours\n")
validate_and_execute()