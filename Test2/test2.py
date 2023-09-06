while True:
    num1 = int(input("Please input the first integer: "))
    num2 = int(input("Please input the second integer: "))

    print("\nChoose an Operation:")
    print("1: ADDITION")
    print("2: SUBTRACTION")
    print("3: MULTIPLICATION")
    print("4: DIVISION")

    choice = input("Enter the operation required (1/2/3/4): ")

    if choice not in ('1', '2', '3', '4'):
        print("Invalid Choice, please choose a valid option.")
        continue

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
            print("ERROR: Division by zero is not allowed. Please choose another option.")
            continue
        else:
            result = num1 / num2
            operation = "Division"

    print(f"The result of {operation} between {num1} and {num2} is equal to {result}")

    num3 = int(input("Please input the third integer: "))

    print("\nChoose an Operation for the result and the third integer:")
    print("1: ADDITION")
    print("2: SUBTRACTION")
    print("3: MULTIPLICATION")
    print("4: DIVISION")

    choice = input("Enter the operation required (1/2/3/4): ")

    if choice not in ('1', '2', '3', '4'):
        print("Invalid Choice, please choose a valid option.")
        continue

    if choice == '1':
        result += num3
        operation = "Addition"
    elif choice == '2':
        result -= num3
        operation = "Subtraction"
    elif choice == '3':
        result *= num3
        operation = "Multiplication"
    elif choice == '4':
        if num3 == 0:
            print("ERROR: Division by zero is not allowed. Please choose another option.")
            continue
        else:
            result /= num3
            operation = "Division"

    print(f"The result of {operation} between the previous result and {num3} is equal to {result}")

    another_operation = input("Do you want to perform another operation with a different third integer? (yes/no): ")
    if another_operation.lower() != 'yes':
        break
