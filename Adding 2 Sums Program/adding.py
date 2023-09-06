#Assign two variables as integers
num1 = int(input("Enter First Number to be added: "))
num2 = int(input("Enter Second Number to be added: "))
#create a new variable that adds num1 and num2
result = num1 + num2
#Create a new variable that gets the remainder of result.
remainder = result % 2

print ("The result for the addition of ", num1, "+", num2, "is equal to", result)

#if the remainder is 0, output that the result is an even number if not, output that the result is an odd number with a remainder of [REMAINDER]
if (remainder == 0):
    print(result,"is an Even Number.")
else:
    print (result, "is an Odd Number with a Remainder of ",remainder)
