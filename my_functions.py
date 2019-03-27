# Module containing my usefull functions


def letter_counter(string, letter="A"):
    letter_counter = 0
    try:
        for element in string:
            if element.lower() == letter.lower():
                letter_counter += 1
    except Exception:
        print("Could not complete the action!")
    return letter_counter
