def check_if_todo(text):
    if text == "":
        raise Exception("Text cannot be empty")
    if "TODO:" in text.upper() or "TODO " in text.upper():
        return True
    elif "TO DO:" in text.upper() or "TO DO " in text.upper() or text.upper()[-2:] =='DO':
        return True
    else:
        return False