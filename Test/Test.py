while True:
    age = int(input("Please input your age group here: "))

    if age <= 0:
        print ("You are not born yet.")

    elif 0 <= age <= 19:
        print("Your age is between that of a newborn and a teenager.")

    elif 20 <= age <= 59: 
        print("Your age is between that of an Adolescent and Late Adult.")

    elif 60 <= age <= 99:
        print("You are probably an elderly or a dead person")

    elif age >= 100:
        print("You are most likely dead.")

    another_age = input("Do you want to calculate using a different age? (yes/no): ").lower()
    if another_age != 'yes':
        break