def load_data(filepath):
    list_of_words = open(filepath, "r", encoding="utf-8").read().lower().split()
    return list_of_words
    #У меня не получилось вернуть список при использовании with open


def get_most_frequent_words(text):
    list_sorted = sorted([add for add in set(text) if len(add)>0 ], key=text.count, reverse=True)
    #"add" is a variable to add words in set if these are not empty
    return list_sorted


def print_only_10_common_words(list_to_get_words_from):
    counter = 10
    for word_print in list_to_get_words_from:
    	if counter == 0:
    		break
    	else:
    		counter -= 1
    		print(word_print, end=", ")

if __name__ == '__main__':
    users_filepath = input("Enter the path to the file: \n")
    words_list = load_data(users_filepath)
    words_list = get_most_frequent_words(words_list)
    print_only_10_common_words(words_list)
