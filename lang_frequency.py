import re
import collections


def load_and_format_data(filepath):
    with open(filepath, "r", encoding="utf-8") as words:
        words_list = words.read().lower()
        words_list = re.sub(r'[\W]', ' ', words_list)
        return re.split(r' ', words_list)


def most_common_words(text):
    counted_words_in_dict = collections.Counter(text)
    return counted_words_in_dict


def print_most_common_words(get_words, words_amount):
    print("Top-{} common words: ".format(words_amount))
    for word_print, counter_of_printing in get_words.most_common(words_amount):
        print('%s: %d' % (word_print, counter_of_printing), end="; ")


if __name__ == '__main__':
    users_filepath = input("Enter the path to the file: \n")
    words_amount = 10
    words_list = load_and_format_data(users_filepath)
    words_list = most_common_words(words_list)
    print_most_common_words(words_list, words_amount)
