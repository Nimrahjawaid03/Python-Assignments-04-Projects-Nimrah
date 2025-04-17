# This program Print 10 random numbers in the range 1 to 100.
import random
number_range = 10
min_value = 1
max_value = 100
def main():
    print("Generate Random Numbers")
    for i in range(number_range):
        random_numbers = random.randint(min_value, max_value)
        print(random_numbers)
  

if __name__ == "__main__":
    main()    