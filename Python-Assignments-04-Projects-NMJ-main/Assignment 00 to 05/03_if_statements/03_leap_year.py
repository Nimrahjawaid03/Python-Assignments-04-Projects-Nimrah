# Write a program that reads a year from the user and tells whether a given year is a leap year or not.
def main():
    print("Check for a leap year")
    user_input = int(input("Enter year : "))
    if user_input % 4 == 0:
        if user_input % 100 == 0:
            if user_input % 400 == 0:
                print("That's a leap year!")
            else:
                print("That's not a leap year.")    
        else:
            print("That's not a leap year.")    
    else:
        print("That's not a leap year.")    
        
if __name__ == "__main__":
    main()        