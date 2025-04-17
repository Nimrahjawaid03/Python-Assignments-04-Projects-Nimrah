# Write a function that takes two numbers and finds the average between the two.
def average(a:float, b:float):
    sum = a + b
    return sum/2

def main():
    average1 = average(0, 10)
    average2 = average(8, 10)
    final_average = average(average1, average2)
    
    print("Average 1 = ", average1)
    print("Average 2 = ", average2)
    print("Final Average = ", final_average)
    
if __name__ == "__main__":
    main()    