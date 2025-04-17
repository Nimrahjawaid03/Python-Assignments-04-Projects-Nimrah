# This program asks the user for two integers and prints their sum.
def main():
    print("This program asks the user for two integers and print their sum")
    try:
        number1 : str = input("Enter First Number ")
        number1 : int = int(number1)
    
        number2 : str = input("Enter Second Number")
        number2 : int = int(number2)
        result = number1 + number2
        print(f"The sum is {result}")
    except ValueError:
        print("Please enter valid integers.")  
             
if __name__ == "__main__":
    main()    