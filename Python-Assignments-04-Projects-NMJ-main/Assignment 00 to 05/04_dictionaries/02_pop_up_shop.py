# Program that loops through a dictionary of fruits, prompting the user to see how many of each fruit they want to buy, and then prints out the total combined cost of all fruits.
def main():
    print("print total combined cost of all fruits.")
    fruits = {'apple': 1.5, 'durian': 50, 'jackfruit': 80, 'kiwi': 1, 'rambutan': 1.5, 'mango': 5}
    
    total_cost = 0
    for fruit in fruits:
        price = fruits[fruit]
        amount_bought = int(input("How many (" + fruit + ") do you want to buy?: "))
        if amount_bought == "":
            break
        total_cost += (price * amount_bought)
    
    print("Your total is $" + str(total_cost))


if __name__ == '__main__':
    main()     