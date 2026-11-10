# 🍕 Day 3 — Python Pizza Deliveries

# TODO 1: Create a greeting for your Pizza Delivery program.
# TODO 2: Ask the user what size pizza they want and store it in a variable.
# Example: S, M or L
# TODO 3: Ask the user if they want pepperoni and store their answer in a variable.
# Example: Y or N
# TODO 4: Ask the user if they want extra cheese and store their answer in a variable.
# Example: Y or N
# TODO 5: Create a bill variable and set its initial value to 0.
# TODO 6: Calculate the base price based on the pizza size.
# Small = $15
# Medium = $20
# Large = $25
# Hint: Use if, elif and else.
# TODO 7: Add the pepperoni cost based on the user's choice.

# Small pizza + pepperoni = $2
# Medium/Large pizza + pepperoni = $3

# Hint: You will need a nested if.
# TODO 8: Add the extra cheese cost if the user chooses it.

# Extra cheese = $1
# TODO 9: Print the final bill.

# Example: Your final bill is: $24
# TODO 10: If the user enters an invalid pizza size, show an error message.
print("""
██████  ██ ███████ ███████  █████      ██████  ███████ ██      ██ ██    ██ ███████ ██████  ██    ██ 
██   ██ ██    ███     ███  ██   ██     ██   ██ ██      ██      ██ ██    ██ ██      ██   ██  ██  ██  
██████  ██   ███     ███   ███████     ██   ██ █████   ██      ██ ██    ██ █████   ██████    ████   
██      ██  ███     ███    ██   ██     ██   ██ ██      ██      ██  ██  ██  ██      ██   ██    ██    
██      ██ ███████ ███████ ██   ██     ██████  ███████ ███████ ██   ████   ███████ ██   ██    ██    
                                                                                                   
""")

user_pizza_size = input("What pizza size do you want:\nSmall :S\nMedium: M\nLarge: L\nChoose:").upper()

want_pepperoni = input("Do you want Pepperoni🌶️🫑 (yes 'Y' or No 'N'):").upper()

want_extra_cheese = input("Do you want Extra Cheese🧀 (yes 'Y' or No 'N'):").upper()

total_bill = 0

# Example: You have chosen an invalid size.
if user_pizza_size == "S":
    total_bill = 15
    if want_pepperoni == "Y":
        total_bill += 2
    if want_extra_cheese == "Y":
        total_bill += 1
elif user_pizza_size == "M":
    total_bill = 20
    if want_pepperoni == "Y":
        total_bill += 3
    if want_extra_cheese == "Y":
        total_bill += 1

elif user_pizza_size == "L":
    total_bill = 25
    if want_pepperoni == "Y":
        total_bill += 3
    if want_extra_cheese == "Y":
        total_bill += 1
else:
    print("You have chosen an invalid 🍕 size.")

print("\n========= Order ===========")
print(f"Pizza size : {user_pizza_size}")
print(f"Pepperoni : {want_pepperoni}")
print(f"Extra cheese : {want_extra_cheese}")
print(f"Final Bill :💲{total_bill}")
