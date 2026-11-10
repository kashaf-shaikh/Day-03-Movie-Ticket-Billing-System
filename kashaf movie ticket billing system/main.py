# TODO 1: Create a greeting for your Movie Ticket Billing System.

print("""
  __  __            _        _______ _      _        _                    _                 
 |  \/  |          (_)      |__   __(_)    | |      | |                  | |                
 | \  / | _____   ___  ___     | |   _  ___| | _____| |_    ___ _   _ ___| |_ ___ _ __ ___  
 | |\/| |/ _ \ \ / / |/ _ \    | |  | |/ __| |/ / _ \ __|  / __| | | / __| __/ _ \ '_ ` _ \ 
 | |  | | (_) \ V /| |  __/    | |  | | (__|   <  __/ |_   \__ \ |_| \__ \ ||  __/ | | | | |
 |_|  |_|\___/ \_/ |_|\___|    |_|  |_|\___|_|\_\___|\__|  |___/\__, |___/\__\___|_| |_| |_|
                                                                 __/ |                      
                                                                |___/                       
""")
# TODO 2: Ask the user for their age and convert the input into an integer.
user_age = int(input("what is your age 🥸?"))
# TODO 3: Ask the user what type of ticket they want and store it in a variable.
ticket = input("What type of ticket they want :\nPremium: P\nRegular: R\nSelect:").upper()
# Example: R or P
# TODO 4: Create a bill variable and set its initial value to 0.
bill = 0
# TODO 5: Calculate the ticket price based on the ticket type.
if ticket == "R":
    bill = 10
elif ticket == "P":
    bill = 15
else:
    print("Please select a valid ticket ('premium' or 'regular')🎫")
# Regular = $10
# Premium = $15

# Hint: Use if and elif.
if ticket == "R" or ticket == "P":
    discount = None
    # TODO 6: Apply a discount based on the user's age.
    if user_age < 13:
        discount = 3
    elif user_age >=60:
        discount = 2
    # Age below 13 = $3 discount
    # Age 60 or above = $2 discount

    # Hint: Use if and elif.
    # TODO 7: Ask the user if they want popcorn.
    want_popcorn = input("Do you want Popcorn🍿 while watching a movie🎞🎥?").upper()
    # Example: Y or N
    # TODO 8: Add $5 to the bill if the user wants popcorn.
    if want_popcorn == "Y":
        bill += 5
    # Hint: Use if.
    # TODO 9: Calculate the final amount after applying the discount.
    final_bill = bill
    if discount is None:
        print("No Discount is Available!😊")
    else:
        final_bill = bill - discount
    # TODO 10: Print the final bill.
    print("\n======= Final Bill ==========")
    print(f"Ticket : {ticket}")
    print(f"Popcorn: {want_popcorn}")
    print(f"Before Discount : 💲{bill}")
    print(f"After Discount of {discount}\nFinal Bill : 💲{final_bill}")

# Example: Your final bill is: $12