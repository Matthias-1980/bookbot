# Assuptions:
#   That there exists a text file to read.
#   That text file should be inside a folder called books.
# Expected behaviour:
#   N + C 
#   Counts number of words and letters in read book.
# Encapsulation change:
def main():
    book_to_read = "books/frankenstein.txt"
    file_content = get_file_data(book_to_read)
    count_of_words = get_numwords(file_content)
    num_letters = get_num_letters(file_content)
    sorted_list = sort_list(num_letters)
    display_data(book_to_read, count_of_words, sorted_list)

def get_file_data(location):
    with open(location) as f:
        file_content = f.read()
    return file_content

def get_numwords(file_content):
    return len(file_content.split())

def get_num_letters(phrase):
    letter_dictionary = {}
    for letter in phrase:
        if letter.isalpha():
            if letter.lower() in letter_dictionary:
                letter_dictionary[letter.lower()] += 1
            else:
                letter_dictionary[letter.lower()] = 1
            
    
    return letter_dictionary

def sort_list(num_letters):
    list_to_sort = list()
    for _key in num_letters:
        temp_dict = dict()
        temp_dict["name"] = _key
        temp_dict["num"] = num_letters[_key]
        list_to_sort.append(temp_dict)

    list_to_sort.sort(reverse=True, key=sort_on)
    return list_to_sort

def sort_on(dict):
    return dict["num"]

def display_data(book_to_read, count_of_words, sorted_list):
    print(f"--- Begin report of {book_to_read} ---")
    print(f"{count_of_words} words found in the document")
    print("")
    for _dict in sorted_list:
        print(f"The '{_dict["name"]}' character was found {_dict["num"]} times")

    print("--- End report ---")

main()
