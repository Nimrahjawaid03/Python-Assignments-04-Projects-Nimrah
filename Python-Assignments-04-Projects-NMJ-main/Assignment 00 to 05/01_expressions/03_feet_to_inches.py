# This program asks user for feet and convert them into inches

inches_in_feet = 12
def main():
    print("Converting feet to inches")
    feet:float = float(input("Enter the number of feet "))
    conversion = feet * inches_in_feet
    print(f"{feet} are equal to {conversion} inches")

if __name__ == "__main__":
    main()    