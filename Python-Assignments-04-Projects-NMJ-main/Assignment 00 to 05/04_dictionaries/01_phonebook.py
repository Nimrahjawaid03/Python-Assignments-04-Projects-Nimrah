# This program show an example of using dictionaries to keep track of information in a phonebook.
phonebook = {}
def read_phonenumbers():
    while True:
        name = input("enter a name")
        
        if name  == "":
            break
        number = int(input("enter a number"))
        phonebook[name] = number
    return phonebook

def print_phonebook(phonebook):
    for name in phonebook:
        print(name, ":", phonebook[name])
        
def search_phone(phonebook): 
    while True:
        name = input("enter name to search")
        if name == "":
            break
        if name not in phonebook:
            print(name, "is not in phonebook ")   
        else:
            print(name, ":", phonebook[name])
                
def main():
    phonebook = read_phonenumbers()
    print_phonebook(phonebook)
    search_phone(phonebook)     
    

if __name__ == '__main__':
    main()