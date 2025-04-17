#This program asks the user for lengths of the two perpendicular sides of a right triangle and outputs the length of the third side (the hypotenuse) using the Pythagorean theorem!
import math

def main():
    print("Get the two side lengths from the user")
    side1_ab:float = float(input("Enter side 1 "))
    side2_ac:float = float(input("Enter side 2 "))
    
    bc:float = math.sqrt(side1_ab**2 + side2_ac**2)
    print(f"The length of (the hypotenuse) BC is: {bc}")
    
if __name__ == "__main__":
    main()    