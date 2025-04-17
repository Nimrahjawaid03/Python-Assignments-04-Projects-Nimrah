# This function collects the user's first name, last name, and email and returns them as a tuple.

def get_user_data():
    first_name_input = input("Enter your first name : ")
    last_name_input = input("Enter your last name : ")
    email_input = input("Enter your email : ")
    return first_name_input, last_name_input, email_input

def main():
    user_data = get_user_data()
    print("Received the following user data:", user_data)
    
if __name__ == "__main__":
    main()    