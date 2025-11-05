name= input("Enter your full name: ")
hometown= input("Enter your hometwon: ")

# Keep asking for age until the user enters a valid number
while True:
    try:
        age= int(input("Enter your age: "))
        break
    except ValueError:
        print("Please enter a valid number.")

# Storing user info in a dictionary
person_info={
    "name": name,
    "hometown": hometown,
    "age":age
}

# Display information using formatted output
print(f"\nName: {person_info['name']}\nHometown: {person_info['hometown']}\nAge: {person_info['age']}")