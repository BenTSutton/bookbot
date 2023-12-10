def main():
    path_to_file = "books/frankenstein.txt"
    print_report(path_to_file)
    

def get_book(path):
    with open(path) as f:
        return(f.read())
    
def word_count(book):
    words = book.split()
    return(len(words))

def letter_count(book):
    letters = {}
    for letter in book:
        lower_case_letter = letter.lower()
        if lower_case_letter in letters:
            letters[lower_case_letter] += 1
        elif letter.isalpha():
            letters[lower_case_letter] = 1
    return(letters)

def sort_letters_dict_to_list(dict):
    sorted_list = []
    for letter in dict:
        sorted_list.append({"letter": letter, "number_of_occurances": dict[letter]})

    sorted_list.sort(reverse=True, key=sort_key)
    return sorted_list

def sort_key(e):
    return e["number_of_occurances"]


def print_report(path):
    print(f"--- Begin report of {path} ---")
    book = get_book(path)
    book_word_count = word_count(book)
    print(f"{book_word_count} words found in the document\n\n")
    letter_dict = letter_count(book)

    sorted_letters = sort_letters_dict_to_list(letter_dict)
    print(sorted_letters)

    for letter in sorted_letters:
        print(f"The '{letter['letter']}' character was found {letter['number_of_occurances']}")
    


main()