# This program generates and prints 10 random numbers between 1 and 100 each time it runs.

import random

N_NUMBERS = 10
MIN_VALUE = 1
MAX_VALUE = 100

def main():
    print("Generate and print 10 random numbers between 1 and 100")
    for _ in range(N_NUMBERS):
        print(random.randint(MIN_VALUE, MAX_VALUE))

if __name__ == '__main__':
    main()