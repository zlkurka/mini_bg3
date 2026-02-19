from string import ascii_uppercase

def menu(options=list, menu_text=str):

    # Acceptable list item types:
        # str
        # Enum child class
        # int
        # float
    # List item types that would print but would be weird
        # array
        # tuple
        # dict
    
    # Multiple different types are acceptable!

    # Printing menu
    print(menu_text)
    for item_num in range(len(options)):
        
        try:
            print(f'{ascii_uppercase[item_num]}) {options[item_num].name}')
        except AttributeError:
            print(f'{ascii_uppercase[item_num]}) {str(options[item_num])}')
        # Will print like "A) Squid"

    # Taking input and translating to list item
    while True:

        selection = input().upper().strip()

        if selection not in list(ascii_uppercase):
            print('Invalid input! Enter only the letter corresponding to your selection.')
            continue
        
        if list(ascii_uppercase).index(selection) > len(options) - 1:
            print('Invalid input! This letter does not correspond to an option.')
            continue
        
        return options[list(ascii_uppercase).index(selection)]