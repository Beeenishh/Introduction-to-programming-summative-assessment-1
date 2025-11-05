print("Welcome to my European capitals quiz!")

# List of countries
countries = ["France", "Italy", "Germany", "Spain", "Portugal", 
             "Netherlands", "Belgium", "Sweden", "Norway", "Switzerland"]
# List of matching capitals
capitals = ["Paris", "Rome", "Berlin", "Madrid", "Lisbon", 
            "Amsterdam", "Brussels", "Stockholm", "Oslo", "Bern"]

# Start score at 0
score = 0

# Loop through each country in the list
for i in range(len(countries)):
    answer = input(f"What is the capital of {countries[i]}? ").lower()
    
     # Check if the user's answer matches the correct capital
    if answer == capitals[i].lower():
        print("That's right!\n")

        # Add 1 to score for a correct answer
        score += 1
    else:
        print(f"Nope, it's {capitals[i]}.\n")

# Shows the final score using an f-string to display how many they got right
print(f"You got {score} out of {len(countries)} right.")
print("Thanks for playing!")