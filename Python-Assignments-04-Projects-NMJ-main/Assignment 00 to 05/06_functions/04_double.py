# This program ask for a int input and return its double number
def double_number(num: int):
    num * 2
    
def  main():
    print("Double the number")
    user_input = input("Enter a number to double : ")
    double = double_number(user_input)
    print("Double number is : ", double)
    
if __name__ == "__main__":
    main()        