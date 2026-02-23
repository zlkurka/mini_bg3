from tools.character import Companion, Monster

def print_list(items=list, text=str):
    
    # I can't believe I have to do this, but otherwise the conversion it does 
    # to print items converts the actual list in the main function. Wtf
    items = list(items)

    for itm in items:
        if type(itm) == Companion or type(itm) == Monster:
            items[items.index(itm)] = itm.name

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