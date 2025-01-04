path_to_file = "books/frankenstein.txt"

def main():
    with open(path_to_file) as f:
        file_contents = f.read()
    word_count = count_words(file_contents)
    character_dict = count_characters(file_contents)
    character_list = []
    
    for dict in character_dict:
        temp = {dict: character_dict[dict]}
        character_list.append(temp)
    character_list.sort(reverse=True, key=get_value)

    print(f"--- Begin report of {path_to_file} ---")
    print(f"{word_count} words found in the document")
    for i in range(0, len(character_list)):
        character = next(iter(character_list[i]))
        print(f"The '{character}' character was found {character_list[i][character]} times")
    print("--- End report ---")

def get_value(single_dict):
    return list(single_dict.values())[0]

def count_words(book):
    return len(book.split())

def count_characters(book):
    characters = {}
    lowered_book = book.lower()
    for letter in lowered_book:
        if letter.isalpha():
            if letter in characters:
                characters[letter] += 1
            else:
                characters[letter] = 1
    return characters

main()