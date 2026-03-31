from rich import print

def print_list(items: list, text: str):

    print(text, end=" ")
    
    if len(items) == 2:
        print(str(items[0]), "and", str(items[1]), end="!\n")
        # This wouldn't be necessary if you don't use the Oxford comma, just remove the comma from 2nd to last item below
        return

    for itm in items:
        
        if (len(items) - 1) - items.index(itm) >= 2:
            # e.g., item 0 or 1 of 4
            print(str(itm), end=", ")
        
        if (len(items) - 1) - items.index(itm) == 1:
            # e.g., item 2 of 3 or 3 of 4
            print(str(itm), end=", and ")
            # Oxford comma
        
        if (len(items) - 1) - items.index(itm) == 0:
            # last item in list
            print(str(itm), end="!\n")