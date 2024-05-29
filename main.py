def main():
    book_to_read = "books/frankenstein.txt"
    file_content = get_file_data(book_to_read)
    count_of_words = get_numwords(file_content)
    num_letters = get_num_letters(file_content)
    print(count_of_words)
    print(num_letters)

def get_file_data(location):
    with open(location) as f:
        file_content = f.read()
    return file_content

def get_numwords(file_content):
    return len(file_content.split())

def get_num_letters(phrase):
    letter_dictionary = {}
    for letter in phrase:
        if letter.lower() in letter_dictionary:
            letter_dictionary[letter.lower()] += 1
        else:
            letter_dictionary[letter.lower()] = 1
            
    
    return letter_dictionary


main()
