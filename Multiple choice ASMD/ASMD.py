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
        #Allows the user to choose another operation if the 2nd integer input is equals to zero as division to zero is not possible.
        if num2 == 0:
            print("ERROR! : Division by zero is not allowed. Please choose another option. ")
            continue
        #Proceed with the operation if the integer given is not equal to zero.
        else:
            result = num1 / num2
            operation = "Division"
<<<<<<< HEAD
=======
            break
    #If the user choice is not the ones within the if else arguments, print out else which says Invalid Choice and make the user choose another operation.
>>>>>>> 45b2c45bb765c6cca6d7b23986c85e540bcceb4c
    else:
        print("Invalid Choice, please choose a valid option. ")

    #Get a choice from the four choices in the if-else commands.
    if choice in ('1', '2', '3', '4'):
        print(f"\n\nThe result of {operation} between {num1} and {num2} is equal to {result}\n\n")

    #Add a new input which asks the user if they want to know if the integer is an odd or even integer.
    odd_even = input("Do you want to know if the Result is an Odd or Even Integer? [yes/no]: ")
    #If the user prompt is yes, proceed with showing results whether the result is odd or even.
    if odd_even == "yes":
        if result % 2 == 0:
            print("The result ", result  ,"is an Even Integer. \n")
        else:
<<<<<<< HEAD
            print ("The result ", result ,"is an odd integer. \n\n")
=======
            print ("The", result ,"is an odd integer. \n\n")
# If user chooses no, end the program.
>>>>>>> 45b2c45bb765c6cca6d7b23986c85e540bcceb4c

#asks the user if they want to conduct another operation based on the integers previously given.
    another_calculation = input("Do you want to calculate using a different operation? (yes/no): ").lower()
    if another_calculation != 'yes':
# End the program if the user chooses no.
        break  # Exit the program if the user chooses to quit
