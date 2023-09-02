#assigns number as an integer input with the text "Enter a Number to be Processed".
number = int(input("Enter a number to be processed "))

#assigns 
remainder = number % 2

if (remainder == 0):
    print(number, "is an even number.")
else:
    print(number, "is an odd number with a remainder of", remainder)