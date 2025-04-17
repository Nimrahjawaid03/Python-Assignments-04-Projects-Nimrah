# Simulate rolling two dice, and prints results of each roll as well as the total.
import random

dice_side = 6

def main():
    print("Starting game...")
    die1 = random.randint(1, dice_side)
    die2 = random.randint(1, dice_side)
    total = die1 + die2
    
    print("Side of Dice =", dice_side)
    print("First die =", die1)
    print("Second die =", die2)
    print("Total of dice =", total)
    
if __name__ == "__main__":
    main()    