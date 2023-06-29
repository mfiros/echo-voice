import json


def convert_to_keypad(word):
    keypad_mapping = {
        'a': '2', 'b': '2', 'c': '2',
        'd': '3', 'e': '3', 'f': '3',
        'g': '4', 'h': '4', 'i': '4',
        'j': '5', 'k': '5', 'l': '5',
        'm': '6', 'n': '6', 'o': '6',
        'p': '7', 'q': '7', 'r': '7', 's': '7',
        't': '8', 'u': '8', 'v': '8',
        'w': '9', 'x': '9', 'y': '9', 'z': '9'
    }
    keypad_word = ''
    for char in word:
        if char.lower() in keypad_mapping:
            keypad_word += keypad_mapping[char.lower()]
    return keypad_word


def load_word_list(file_path):
    with open(file_path, 'r') as file:
        word_list = [word.strip().lower() for word in file.readlines()]
    return word_list


def filter_words_by_length(word_list, length):
    filtered_words = [word for word in word_list if len(word) == length]
    return filtered_words


def generate_word_dictionary(file_path, length):
    word_list = load_word_list(file_path)
    words = filter_words_by_length(word_list, length)
    keypad_words = {word: convert_to_keypad(word) for word in words}
    return keypad_words


def save_word_dictionary_to_json(word_dictionary, output_file):
    with open(output_file, 'w') as file:
        json.dump(word_dictionary, file, indent=4)


file_path = 'english.txt'  # Replace with the actual file path on your system
word_length = 4  # Replace with the desired word length
# Replace with the desired output file name
output_file = 'words_dictionary4.json'

word_dictionary = generate_word_dictionary(file_path, word_length)
save_word_dictionary_to_json(word_dictionary, output_file)
