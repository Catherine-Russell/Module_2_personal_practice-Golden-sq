def get_most_common_letter(text):
    counter = {}
    for char in text:
        if char.isalpha():
            counter[char] = counter.get(char, 0) + 1
    print(f"The dictionary looks like this: {counter}")
    print(f"when it's sorted, it looks like this: {sorted(counter.items(), key=lambda item: item[1])}")
    letter = sorted(counter.items(), key=lambda item: item[1])[-1][0]
    print(letter)
    return letter


print(f"""
Running:  get_most_common_letter("the roof, the roof, the roof is on fire!"))
Expected: o
Actual:   {get_most_common_letter("the roof, the roof, the roof is on fire!")}
""")