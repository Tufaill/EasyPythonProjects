#This small work justifies that i have understood the concept of nested,multi if, elif

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
age_less_12 = 5
age_less_18 = 7
age_greater_18 = 12

if height>=120:
    age = int(input("enter age: "))
    if age < 12:
        print(f"Please pay {age_less_12}$.")
    elif age<18:
        print(f"Please pay {age_less_18}$.")
    else:
        print(f"Please pay {age_greater_18}$.")

#we will add +3 dollar for photo
    photo = input("Do you want to take a photo: ")
    age_less_12 += 3
    age_less_18 += 3
    age_greater_18 += 3
    if photo == "yes":
        if age < 12:
            print(f"With photo please pay {age_less_12}")
        elif age<18:
            print(f"With photo please pay {age_less_18}")
        else:
            print(f"With photo please pay {age_greater_18}")
    else:
        print("Please pay for the ride only")
else:
    print("Sorry you have to grow taller before you can ride")








