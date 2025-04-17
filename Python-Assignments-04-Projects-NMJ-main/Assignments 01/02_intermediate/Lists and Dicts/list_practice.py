# This program demonstrates basic list operations: creating a list, checking its length, and appending an item.
def main():
    fruit_list = ['apple', 'banana', 'orange', 'grape', 'pineapple']
    
    print("Length of the list:", len(fruit_list))
    
    fruit_list.append('mango')
    
    print("Updated list:", fruit_list)

if __name__ == '__main__':
    main()