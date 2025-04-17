# This function prints the given message a specified number of times.

def print_multiples(message: str, repeats: int):
    for i in range(repeats):
        print(message)
        
def main():
    print("print given message a specified number of times")
    message = str(input("Enter a message : "))
    repeats = int(input("Number of times to repeat : "))
    print_multiples(message, repeats)
    
if __name__ == "__main__":
    main()    