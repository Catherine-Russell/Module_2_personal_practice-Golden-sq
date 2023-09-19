def make_snippet(str):
    words = len(str.split())
    if words <= 5:
        return str
    else:
        snippet = str.split()[:5]
        return " ".join(snippet) + "..."
    
def count_words(strng):
    if strng.isdigit():
        raise Exception("Please input words, not numbers")
    else:
        return len(strng.split())