# This program helps practice list operations like accessing, modifying, and slicing elements through a simple interactive game.
def access_element(my_list, index):
    """
    Returns the element at the specified index in the list.
    If the index is out of range, returns an appropriate message.
    """
    if 0 <= index < len(my_list):
        return my_list[index]
    else:
        return "Index out of range."

def modify_element(my_list, index, new_value):
    """
    Replaces the element at the specified index with the new value.
    If the index is out of range, returns an appropriate message.
    """
    if 0 <= index < len(my_list):
        my_list[index] = new_value
        return f"Element at index {index} has been changed to {new_value}."
    else:
        return "Index out of range."

def slice_list(my_list, start_index, end_index):
    """
    Returns a new list containing elements from the start index up to (but not including) the end index.
    Handles cases where indices are out of range.
    """
    if 0 <= start_index < len(my_list) and 0 <= end_index <= len(my_list):
        return my_list[start_index:end_index]
    else:
        return "Invalid range."

def game():
   
    my_list = [10, 'apple', 3.14, 'banana', 'grape']

    while True:
        print("\nCurrent list:", my_list)
        print("Select an operation:")
        print("1. Access element")
        print("2. Modify element")
        print("3. Slice the list")
        print("4. Exit")

        choice = input("Enter 1, 2, 3, or 4: ")

        if choice == '1': 
            index = int(input("Enter the index to access: "))
            result = access_element(my_list, index)
            print(f"Result: {result}")
        
        elif choice == '2':
            index = int(input("Enter the index to modify: "))
            new_value = input("Enter the new value: ")
            result = modify_element(my_list, index, new_value)
            print(f"Result: {result}")
        
        elif choice == '3': 
            start_index = int(input("Enter the start index: "))
            end_index = int(input("Enter the end index: "))
            result = slice_list(my_list, start_index, end_index)
            print(f"Result: {result}")
        
        elif choice == '4':
            print("Thanks for playing!")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    game()