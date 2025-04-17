# This function checks if the given age is greater than or equal to the legal adult age (18).

ADULT_AGE :int = 18 
def is_adult(age : int):
    if age >= ADULT_AGE:
        return True
    return False

def main():
    user_age = int(input("Enter your age : "))
    print(is_adult(user_age))
    
if __name__ == "__main__":
    main()    