import re
import collections


def load_and_format_data(filepath):
    with open(filepath, "r", encoding="utf-8") as words:
        data = words.read()
        data = re.sub(r'[\W]', ' ', data)
        data = re.split(r' ', data)
        return data


def get_most_frequent_words(text):
    counted_words_in_dict = collections.Counter(text)
    return counted_words_in_dict


def print_most_common_words(get_words, words_amount):
    print("Top-10 common words: \n")
    for word_print, counter_of_printing in get_words.most_common(words_amount):
        print('%s: %d' % (word_print, counter_of_printing), end="; ")


if __name__ == '__main__':
    users_filepath = input("Enter the path to the file: \n")
    words_list = load_and_format_data(users_filepath)
    words_list = get_most_frequent_words(words_list)
    print_most_common_words(words_list, 10)
