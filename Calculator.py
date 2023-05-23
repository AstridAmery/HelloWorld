
def addition(UserValue1, UserValue2):
    user_output = int(UserValue1 + UserValue2)
    return user_output


def subtraction(UserValue1, UserValue2):
    user_output = UserValue1 - user_value2
    return user_output


def division(UserValue1, UserValue2):
    user_output = UserValue1 / user_value2
    return user_output


def multiplication(UserValue1, UserValue2):
    user_output = UserValue1 * user_value2
    return user_output


print("Welcome to my calculator program.")


while True:

    operation = input("Please select from the following options -> +, -, /, *, quit: ")

    if operation.lower() == 'quit':
        print("Goodbye.")
        break

    user_value1 = int(input("Please select the first value: "))
    user_value2 = int(input("Please select the second value: "))

    if operation == '+':
        output = addition(user_value1, user_value2)
        print(user_value1, "+", user_value2, "is", + output)

    elif operation == '-':
        output = subtraction(user_value1, user_value2)
        print(user_value1, "-", user_value2, "is", + output)

    elif operation == '/':
        output = division(user_value1, user_value2)
        print(user_value1, "/", user_value2, "is", + output)

    elif operation == '*':
        output = multiplication(user_value1, user_value2)
        print(user_value1, "*", user_value2, "is", + output)

    else:
        print("I didn't understand that...")
