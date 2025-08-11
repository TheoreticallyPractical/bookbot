def get_num_words(text):
        string = str(text)
        word_list = string.split()
        word_count = len(word_list)
        return word_count

def get_chars_dict(characters):
        char_string = characters.lower()
        char_count = {}
        for char in char_string:
                if char not in char_count:
                        char_count[char] = 1
                else: char_count[char] += 1
        return char_count

def sort_on(d):
        return d["num"]

def chars_dict_to_sorted_list(num_chars_dict): 
    sorted_list = []
    for ch, count in num_chars_dict.items():
        sorted_list.append({"char": ch, "num": count})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list
