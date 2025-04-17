# Write a program which prompts the user for an adjective, then a noun, then a verb, and then prints a fun sentence with those words!
start_sentence : str = "Panaversity is fun. I learned to program and used Python to make my"
def main():
    print("Get the three inputs from the user to make the adlib")
    adj_input : str = input("Please type an adjective : ")
    noun_input : str = input("Please type a noun : ")
    verb_input : str = input("Please type a verb : ")
    
    print(start_sentence + " " + adj_input + " " + noun_input + " " + verb_input)
    
if __name__ == "__main__":
    main()    