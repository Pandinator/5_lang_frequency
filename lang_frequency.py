import re
import collections


def load_data(filepath):
    with open(filepath, "r", encoding="utf-8") as words:
        return words.read().lower().split()


def format_data(data_to_format):
    reworked_list_of_words = []
    for word in data_to_format:  # remove any non-dig-alpha char
        word = re.sub(r'[\W$]', '', word)
        reworked_list_of_words.append(word)
    return reworked_list_of_words


def get_most_frequent_words(text):
    list_sorted = collections.Counter(text)
    return list_sorted


def print_only_10_common_words(list_to_get_words):
    print("Top-10 common words: ")
    for word_print, counter_of_printing in list_to_get_words.most_common(10):
        print('%s: %d' % (word_print, counter_of_printing), end="; ")

if __name__ == '__main__':
    users_filepath = input("Enter the path to the file: \n")
    words_list = load_data(users_filepath)
    words_list = format_data(words_list)
    words_list = get_most_frequent_words(words_list)
    print_only_10_common_words(words_list)
