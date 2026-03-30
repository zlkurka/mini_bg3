from string import ascii_uppercase
from rich import print

def menu(options=list, menu_text=str, show_race=bool, show_class=bool, show_hp=bool):

    # Acceptable list item types:
        # str
        # Enum child class
        # int
        # float
        # Custom class or Enum with __repr__
    # List item types that would print but would be weird
        # array
        # tuple
        # dict
    
    # Multiple different types are acceptable!
    
    if show_race == bool:
        show_race = False
    if show_class == bool:
        show_class = False
    if show_hp == bool:
        show_hp = False


    # Printing menu
    
    print(menu_text)
    for iter in range(len(options)):
        
        list_item = options[iter]
        list_item_name = str(list_item).capitalize()
        if "]" in list_item_name:
            item_name_listed = list(list_item_name)
            index_char_after_end_bracket = item_name_listed.index("]") + 1
            item_name_listed.insert(index_char_after_end_bracket, item_name_listed.pop(index_char_after_end_bracket).upper())
            list_item_name = "".join(item_name_listed)

        print(f'{ascii_uppercase[iter]}) {list_item_name}', end='')
        
        if show_race and show_class:
            try:
                print(f", {list_item.race} {list_item.charclass}", end='')
            except AttributeError:
                pass
        elif show_race:
            try:
                print(f", {list_item.race}", end='')
            except AttributeError:
                pass
        elif show_class:
            try:
                print(f", {list_item.char}", end='')
            except AttributeError:
                pass
        
        if show_hp:
            try:
                print(f", {list_item.current_hp} / {list_item.max_hp} HP", end='')
            except AttributeError:
                pass

        print()
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