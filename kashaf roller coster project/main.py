# 📝 Day 3 — Rollercoaster TODO
# TODO 1: Create a greeting for your Rollercoaster program.
# TODO 2: Ask the user for their height in cm and convert the input into an integer.
# Example: 150
# TODO 3: Create a bill variable and set its initial value to 0.
# TODO 4: Check if the user is tall enough to ride the rollercoaster.
# Minimum height = 120 cm
# Hint: Use if and else.
# TODO 5: If the user is tall enough, ask for their age and convert it into an integer.
# Age below 12 = $5
# Age 12–18 = $7
# Age 45–55 = Free
# Everyone else = $12
# TODO 6: Set the ticket price based on the user's age.
# Hint: Use if, elif and else.
# TODO 7: Ask the user if they want a photo taken.

# Example: Y or N
# TODO 8: Add $3 to the bill if the user wants a photo.
# Hint: Use if.
# TODO 9: Print the final bill.
# Example: Your final bill is $15
# TODO 10: If the user's height is below 120 cm, show a message telling them they cannot ride.

# Example: Sorry, you have to grow taller before you can ride.


print(f"""
  _____       _ _                              _                                                          
 |  __ \     | | |                            | |                                                         
 | |__) |___ | | | ___ _ __ ___ ___   __ _ ___| |_ ___ _ __   _ __ ___   __ _ _ __   __ _  __ _  ___ _ __ 
 |  _  // _ \| | |/ _ \ '__/ __/ _ \ / _` / __| __/ _ \ '__| | '_ ` _ \ / _` | '_ \ / _` |/ _` |/ _ \ '__|
 | | \ \ (_) | | |  __/ | | (_| (_) | (_| \__ \ ||  __/ |    | | | | | | (_| | | | | (_| | (_| |  __/ |   
 |_|  \_\___/|_|_|\___|_|  \___\___/ \__,_|___/\__\___|_|    |_| |_| |_|\__,_|_| |_|\__,_|\__, |\___|_|   
                                                                                           __/ |          
                                                                                          |___/           
""")
user_height = int(input("How tall are you in cm..?\n"))
bill = 0
if user_height >= 120:
    print("You can ride the rollercoaster!")
    user_age = int(input("Enter your age..?"))

    if user_age < 12:
        bill = 5
        print("Child tickets are $5.")
    elif 12 <= user_age <= 18 :
        bill = 7
        print("Youth tickets are $7.")
    elif 45 <= user_age <= 55:
        print("Ride is on us enjoy with your family😊")
    else:
        bill = 12
        print("Adult tickets are $12.")

    want_photo = input("Do you want a photo while riding a roller coaster..?").lower()
    if want_photo == "y":
        bill += 3

    print(f"Your final bill is 💲{bill}")
else:
    print("Sorry, you have to grow taller before you can ride.")


