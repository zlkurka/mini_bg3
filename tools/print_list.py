from rich import print

def print_list(items=list, text=str):

    print(text, end=" ")
    
    if len(items) == 2:
        print(items[0], "and", items[1], end="!\n")
        return

    for itm in items:
        
        if (len(items) - 1) - items.index(itm) >= 2:
            # e.g., member 0 or 1 of 4
            print(itm, end=", ")
        
        if (len(items) - 1) - items.index(itm) == 1:
            # e.g., member 2 of 3 or 3 of 4
            print(itm, end=", and ")
        
        if (len(items) - 1) - items.index(itm) == 0:
            # last member of party
            print(itm, end="!\n")