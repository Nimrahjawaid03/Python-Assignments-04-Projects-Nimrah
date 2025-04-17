# This program asks user to enter a number then double that number and print out the result. It will repeat that process until the value is 100 or greater.
def main():
    curr_value = int(input("Enter a number to double : "))
    
    while curr_value < 100:
        curr_value *= 2
        print(curr_value)

if __name__ == "__main__":
    main()        