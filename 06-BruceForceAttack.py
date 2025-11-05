print("Please enter the correct password: \n")

correct_password = "12345"
tries = 5

# Keep asking for the password while the user still has tries left
while tries > 0:
    user_input = input("Enter password: ")

    if user_input == correct_password:
        print("correct password \n")
        break
    else:
         # Reduce the number of tries after a wrong attempt
        tries -= 1 
        if tries > 0:
             # Tell the user how many tries are left
            print(f"Incorrect password. You have {tries} attempt(s) left.\n")
        else:
             # When user uses up all tries
            print("Too many wrong attempts. Authorities have been alerted.\n")