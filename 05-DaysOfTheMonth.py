print("Days of the month")

# Dictionary storing month numbers and their number of days
month_days={
    1: 31,
    2: 28,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31
}
# Ask for user inpuit
try:
    month = int(input("pls enter a month number (1-12): "))
except ValueError:
    print("Invalid number. enter a number from 1 to 12.")
    exit()

# Check if the entered month number is valid
if month in range(1, 13):
    # Leap year adjustment
    if month == 2:
        leap = input("Is it a leap year? (yes/no): ")
        if leap == "yes":
            print("February has 29 days in a leap year.")
        else:
            print("February has 28 days.")
    else:
        print(f"Month {month} has {month_days[month]} days.")
else:
     # Message for invalid month number
    print("Invalid month number. Please enter a number from 1 to 12.")

print("\nThe end")