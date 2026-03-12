from string import ascii_uppercase

def menu(options=list, menu_text=str, show_charclass=bool, show_race=bool, show_hp=bool):

    # Acceptable list item types:
        # str
        # Enum child class
        # int
        # float
        # custom classes with __repr__
        # Enum child classes with __str__
    # List item types that would print but would be weird
        # array
        # tuple
        # dict
    
    # Multiple different types are acceptable!

    # Printing menu
    print(menu_text)
    for item_num in range(len(options)):
        
        letter = ascii_uppercase[item_num]
        option = options[item_num]
        
        print(f'{letter}) {str(option).capitalize()}', end='')

        if show_charclass and show_race:
            try:
                print(f', {option.race} {option.charclass}', end='')
            except AttributeError:
                pass
        elif show_charclass:
            try:
                print(f', {option.charclass}', end='')
            except AttributeError:
                pass
        elif show_race:
            try:
                print(f', {option.race}', end='')
            except AttributeError:
                pass
        if show_hp:
            try:
                print(f', {option.current_hp} / {option.max_hp} HP', end='')
            except AttributeError:
                pass
        
        print()

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