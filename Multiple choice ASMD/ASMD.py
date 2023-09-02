num1 = float(input("Please enter the first variable here: "))
num2 = float(input("Please enter the second variable here: "))

# Choosing an operation
while True:
    print("\n\nChoose an Operation")
    print("1: ADDITION")
    print("2: SUBTRACTION")
    print("3: MULTIPLICATION")
    print("4: DIVISION")

    choice = input("Enter the operation required (1/2/3/4): ")

    # Selected operation code
    if choice == '1':
        result = num1 + num2
        operation = "Addition"
    elif choice == '2':
        result = num1 - num2
        operation = "Subtraction"
    elif choice == '3':
        result = num1 * num2
        operation = "Multiplication"
    elif choice == '4':
        if num2 == 0:
            print("ERROR! : Division by zero is not allowed. Please choose another option. ")
            continue
        else:
            result = num1 / num2
            operation = "Division"
            break
    else:
        print("Invalid Choice, please choose a valid option. ")

    if choice in ('1', '2', '3', '4'):
        print(f"\n\nThe result of {operation} between {num1} and {num2} is equal to {result}\n\n")

    another_calculation = input("Do you want to calculate using a different operation? (yes/no): ").lower()
    if another_calculation != 'yes':
        break  # Exit the program if the user chooses to quit