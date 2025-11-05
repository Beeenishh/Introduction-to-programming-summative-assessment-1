def even_or_odd_by_digit(number):
     # Get the last digit of the number
    last_digit = str(number)[-1]
    if last_digit in "02468":
        # Return a message saying the number is either even or odd
        return f"{number} is even."
    else:
        return f"{number} is odd."

def main():
    num = int(input("Enter any whole number: "))
     # Call the function and print
    result = even_or_odd_by_digit(num)
    print(result)

# Using main so the program only runs when we run this file directly
if __name__ == "__main__":
    main()
