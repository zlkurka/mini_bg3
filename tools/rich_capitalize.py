def rich_capitalize(text) -> str:
    
    text = str(text)

    if text[0] == "[":
        text = list(text)
        index_char_after_end_bracket = text.index("]") + 1
        text.insert(index_char_after_end_bracket, text.pop(index_char_after_end_bracket).upper())
        return "".join(text)
    
    return text.capitalize()