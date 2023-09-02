num1 = int(input("Enter First Number to be added: "))
num2 = int(input("Enter Second Number to be added: "))
result = num1 + num2
remainder = result % 2

print ("The result for the addition of ", num1, "+", num2, "is equal to", result)

if (remainder == 0):
    print(result,"is an Even Number.")
else:
    print (result, "is an Odd Number with a Remainder of ",remainder)
