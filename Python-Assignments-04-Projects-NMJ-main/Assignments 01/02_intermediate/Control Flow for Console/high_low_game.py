# This program implements the High-Low game where the player guesses whether their number is higher or lower than the computer's number.
import random

NUM_ROUNDS = 5 

def main():
    print("Welcome to the High-Low Game!")
    print("--------------------------------")
    
    score = 0 

    for round_num in range(1, NUM_ROUNDS + 1):
        print(f"\nRound {round_num}")
        
        player_number = random.randint(1, 100)
        computer_number = random.randint(1, 100)
        
        print(f"Your number is {player_number}")
        
        guess = input("Do you think your number is higher or lower than the computer's?: ").strip().lower()
        
        while guess not in ["higher", "lower"]:
            print("Please enter either 'higher' or 'lower'.")
            guess = input("Do you think your number is higher or lower than the computer's?: ").strip().lower()
        
        if guess == "higher" and player_number > computer_number:
            print(f"You were right! The computer's number was {computer_number}")
            score += 1
        elif guess == "lower" and player_number < computer_number:
            print(f"You were right! The computer's number was {computer_number}")
            score += 1
        else:
            print(f"Aww, that's incorrect. The computer's number was {computer_number}")
        
        print(f"Your score is now {score}")
    
    print("\nThanks for playing!")

    if score == NUM_ROUNDS:
        print("Wow! You played perfectly!")
    elif score >= NUM_ROUNDS // 2:
        print("Good job, you played really well!")
    else:
        print("Better luck next time!")

if __name__ == '__main__':
    main()