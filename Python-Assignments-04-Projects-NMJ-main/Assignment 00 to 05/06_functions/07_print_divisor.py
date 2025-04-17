# This function prints all the divisors of a given number.

def print_divisors(num : int):
    print("Here are the divisors of ", num)
    for i in range(num):
        curr_divisor = i + 1
        if num % curr_divisor == 0:
            print(curr_divisor)
            
def main():
    user_input = int(input("Enter a number : "))
    print_divisors(user_input)
    
if __name__ == "__main__":
    main()               