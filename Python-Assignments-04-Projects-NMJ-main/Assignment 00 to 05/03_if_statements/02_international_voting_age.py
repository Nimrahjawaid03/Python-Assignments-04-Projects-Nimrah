# Program which asks a user for their age and lets them know if they can or can't vote in the following three fictional countries.
PETURKSBOUIPO_AGE : int = 16
STANLAU_AGE : int = 25
MAYENGUA_AGE : int = 48

def main():
    print("user age for vote")
    user_input = int(input("Enter Your Age : "))
    
    if user_input >= PETURKSBOUIPO_AGE:
        print(f"You can vote in Peturksbouipo where the voting age is {PETURKSBOUIPO_AGE}")
    else:
        print(f"You cannot vote in Peturksbouipo as you are only {user_input} years old")
        
    if user_input >= STANLAU_AGE:
        print(f"You can vote in Stanlau where the voting age is {STANLAU_AGE}")    
    else:
        print("You cannot vote in Stanlau as you are only {user_input} years old")
        
    if user_input >= MAYENGUA_AGE:
        print(f"You can vote in Mayengua where the voting age is {MAYENGUA_AGE}")
    else:
        print(f"You cannot vote in Mayengua as you are only")       
        
if __name__ == "__main__":
    main()             