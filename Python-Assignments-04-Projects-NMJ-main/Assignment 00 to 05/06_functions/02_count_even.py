# This function counts and prints the number of even numbers in the given list.

def count_even(lst):
    count = 0
    for num in lst:
        num % 2 == 0
        count += 1
    print(count)
    
def get_int_list():
    lst = []
    user_input = input("Enter an integer or press enter to stop: ") 
    while user_input != "":
        lst.append(int(user_input))
        user_input = input("Enter an integer or press enter to stop: ")
    return lst 

def main():
    lst = get_int_list()
    count_even(lst)
    
if __name__ == "__main__":
    main()    