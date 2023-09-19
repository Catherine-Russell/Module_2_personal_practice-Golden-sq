import math

def find_mins_and_secs(word_count):
    duration = divmod(word_count, 200)
    mins = duration[0]
    secs = math.ceil((duration[1]/200)*60)
    return (mins, secs)


def turn_into_plain_English(duration):
    if 1 not in duration:
        return f"It will take {duration[0]} minutes and {duration[1]} seconds"
    elif duration[0] == 1:
        return f"It will take 1 minute and {duration[1]} seconds"
    else:
        return f"It will take {duration[0]} minutes and 1 second"


def find_duration(text):
    if text.isdigit():
        raise Exception("Please input words, not numbers.")
    word_count = len(text.split())
    duration = find_mins_and_secs(word_count)
    message = turn_into_plain_English(duration)
    return message
