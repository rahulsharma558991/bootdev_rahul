def get_num_words(text):
    words = text.split()
    return len(words)

def get_num_characters(text):
    char_count = {}
    for ch in text.lower():
        if ch in char_count:
            char_count[ch] += 1
        else:
            char_count[ch] = 1
    return char_count

def sort_on(items):
    return items["num"]

def get_sorted_list_of_dicts(dicts_char_count):
    list_of_dict = []
    for ch, count in dicts_char_count.items():
        if ch.isalpha():
            list_of_dict.append({"char": ch, "num": count})
    list_of_dict.sort(reverse=True, key=sort_on)
    return list_of_dict