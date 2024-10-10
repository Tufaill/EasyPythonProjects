# Small pizza (S): $15
# Medium pizza (M): $20
# Large pizza (L): $25
# Add pepperoni for small pizza (Y or N): +$2
# Add pepperoni for medium or large pizza (Y or N): +$3
# Add extra cheese for any size pizza (Y or N): +$1


small_pizza = 15
medium_pizza = 20
large_pizza= 25
pepperoni_small_pizza = 2
pepperoni_medium_large_pizza = 3
cheese_extra = 1
bill= 0

print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza ? Y or N: ")
extra_cheese = input("Do you want extra cheese ? Y or N: ")

if size == "S":
    if pepperoni == "Y" and extra_cheese == "Y":
        bill = small_pizza + pepperoni_small_pizza + cheese_extra
        print(f"Your total bill with extra cheese and pepperoni is ${bill}")
    elif pepperoni == "Y" and extra_cheese == "N":
        bill = small_pizza + pepperoni_small_pizza
        print(f"Your total bill with extra pepperoni is ${bill}")
    elif pepperoni =="N" and extra_cheese == "Y":
        bill = small_pizza + cheese_extra
        print(f"Your total bill with extra cheese is ${bill}")
    else:
        print(f"Your total Pizza bill is {small_pizza}")

elif size == "M":
    if pepperoni == "Y" and extra_cheese == "Y":
        bill = medium_pizza + pepperoni_medium_large_pizza + cheese_extra
        print(f"Your Medium size Pizza with extra pepperoni and chess is {bill}")
    elif pepperoni == "Y" and extra_cheese == "N":
        bill = medium_pizza + pepperoni_medium_large_pizza
    elif pepperoni == "N" and extra_cheese == "Y":
        bill = medium_pizza + cheese_extra
        print(f"Your medium size pizza with extra chesse is {bill}")
    else:
        print(f"Your medium size Pizza is {medium_pizza}")
elif size == "L":
    if pepperoni == "Y" and extra_cheese == "Y":
        bill = large_pizza + pepperoni_medium_large_pizza + cheese_extra
        print(f"Your large size Pizza with extra pepperoni and chess is {bill}")
    elif pepperoni == "Y" and extra_cheese == "N":
        bill = large_pizza + pepperoni_medium_large_pizza
        print(f"Your large size Pizza with extra pepperoni and chess is {bill}")
    elif pepperoni == "N" and extra_cheese == "Y":
        bill = large_pizza + cheese_extra
        print(f"Your medium size pizza with extra chesse is {bill}")
    else:
        print(f"Your large size pizza is {large_pizza}")
else:
    print("please write valid entry")


