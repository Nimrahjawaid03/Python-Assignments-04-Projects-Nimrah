# This program generate a secret random number and compare with users guess.
import random

def main():
    secret_number = random.randint(1, 99)
    
    print("I am thinking of a number between 1 and 99...")
    
    user_guess = int(input("Enter a guess: "))
  
    while user_guess != secret_number:
        if user_guess < secret_number: 
            print("Your guess is too low")
        else:
            print("Your guess is too high")
            
        print() 
        user_guess = int(input("Enter a new guess: ")) 
        
    print("Congrats! The number was: " + str(secret_number))
    
if __name__ == '__main__':
    main()