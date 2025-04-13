def get_num_words(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        num_words = len(file_contents.split())
    return num_words

def get_char_count(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()

    char_count = {}

    for char in file_contents:
        char = char.lower()

        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    return char_count

def sorted_count(char_count):
    dict_list = []
    for item in char_count:
        temp_dict = {}
        temp_dict["letter"] = item
        temp_dict["num"] = char_count[item]
        dict_list.append(temp_dict)

    def sort_on(dict):
        return dict["num"]
    dict_list.sort(reverse=True, key=sort_on)
    return dict_list
