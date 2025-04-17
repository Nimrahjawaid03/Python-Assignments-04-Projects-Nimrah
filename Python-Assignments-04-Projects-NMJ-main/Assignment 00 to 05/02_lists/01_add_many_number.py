# Write a function that takes a list of numbers and returns the sum of those numbers.
def add_many_numbers(numbers):
    many_numbers : int = 0
    for number in numbers:
        many_numbers += number
    return many_numbers

def main():
    numbers : list[int] = [1, 2, 3 ,4 ,5]    
    sum_of_nums = add_many_numbers(numbers)
    print(sum_of_nums)
    
if __name__ == "__main__":
    main()    
        