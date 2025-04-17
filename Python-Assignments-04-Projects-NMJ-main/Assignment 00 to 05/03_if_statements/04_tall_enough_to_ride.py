# This program asks the user how tall they are and prints whether or not they're taller than a pre-specified minimum height.
minimun_height = 50
def main():
    print("Ask for height....")
    user_input = int(input("Enter your height? : "))
    
    if user_input >= minimun_height:
        print("You are tall enough to ride!")
    
    else:
        print("You're not tall enough to ride, but maybe next year!")    
        
if __name__ == "__main__":
    main()        