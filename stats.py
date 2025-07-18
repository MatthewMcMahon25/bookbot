def get_num_words(text):
    # Split the string into a list of strings
    text_list = text.split()

    # return length of list
    return len(text_list)

def get_character_counts(text):
    count = {}

    text_lower = text.lower()

    for char in text_lower:
        if char in count:
            count[char] += 1
        else:
            count[char] = 1
    
    return count

def sort_on(items):
    return items["num"]

def get_sorted_dictionaries(character_dictionary):
    sorted_list = []

    for key in character_dictionary:
        sorted_list.append({"char": key, "num": character_dictionary[key]})

    sorted_list.sort(reverse=True, key=sort_on)

    return sorted_list