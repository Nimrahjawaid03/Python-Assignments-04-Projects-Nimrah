# This is a simple joke bot that tells a joke when asked for one.

prompt = "What do you want?"
joke = "here is a joke"
sorry = "Sorry i only tell jokes"

def main():
    user_input = input(prompt)
    
    if "joke" in user_input:
        print(joke)
    else:
        print(sorry)
        
if __name__ == "__main__":
    main()            