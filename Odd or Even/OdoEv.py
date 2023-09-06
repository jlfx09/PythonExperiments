#Refer to Adding 2 Sums Program for better understanding

#assigns number as an integer input with the text "Enter a Number to be Processed".
number = int(input("Enter a number to be processed "))

#assigns remainder as a variable that gets the remainder of number by 2.
remainder = number % 2

#If the remainder is 0, output that the number is an even number, if not then output that the result is an odd number with a remainder of the remainder remaining in the remainder variable.
if (remainder == 0):
    print(number, "is an even number.")
else:
    print(number, "is an odd number with a remainder of", remainder)
