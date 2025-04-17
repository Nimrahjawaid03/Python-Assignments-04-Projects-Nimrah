# This program calculates and prints the ages of Anton, Beth, Chen, Drew, and Ethan based on given age relationships.

def main():
    print("Calculate and prints the ages")
    Anton : int = 21
    Beth: int = Anton + 6
    Chen: int = Beth + 20
    Drew: int = Chen + Anton
    Ethan: int = Chen
    
    print(f"Anton is {Anton}")
    print(f"Beth is {Beth}")
    print(f"Chen is {Chen}")
    print(f"Drew is {Drew}")
    print(f"Ethan is {Ethan}")
    
    
if __name__ == "__main__":
    main()    