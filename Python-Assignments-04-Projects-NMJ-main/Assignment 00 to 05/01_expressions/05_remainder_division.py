# Ask the user for two numbers, one at a time, and then print the result of dividing the first number by the second and also the remainder of the division.
def main():
    print("Get the numbers we want to divide")
    
    dividend:int = int(input("Enter a number to divide : "))
    divisor:int = int(input("Enter a number to divide by : "))
    
    quotient = dividend // divisor
    reminder = dividend % divisor
    
    print(f"The result of this division is {quotient} with a remainder of {reminder}")
    
if __name__ == "__main__":
    main()    