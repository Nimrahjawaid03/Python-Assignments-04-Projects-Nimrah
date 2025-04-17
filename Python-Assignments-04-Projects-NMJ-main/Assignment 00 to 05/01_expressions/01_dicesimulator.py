    # Simulate rolling two dice, three times. This program is used to show how variable scope works.
import random

num_side:int = 6

def roll_dice():
    print("Rolling dice")
    die1:int = random.randint(1, num_side)
    die2:int = random.randint(1, num_side)
    total:int = die1 + die2
    print("Total of two dice:", total)
 
def main():
    die1:int = 10
    print("die1 in main() start as :", die1)
    roll_dice()
    roll_dice()
    roll_dice()    
    print("die1 in main() :", die1)
if __name__ == "__main__":
    main()   