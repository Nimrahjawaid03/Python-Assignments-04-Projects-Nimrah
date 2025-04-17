# This program asks the user for a number and prints its square.
def main():
    print("square of number")
    try:
        user_input = float(input("Enter a number to see its square"))
        square = str(user_input) + " squared is " + str(user_input ** 2)
        print(square)
    except ValueError:
        print("Please enter a valid number")    
    
if __name__ == "__main__":
    main()    