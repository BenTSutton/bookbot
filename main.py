def main():
    path_to_file = "books/frankenstein.txt"
    file_contents = get_book(path_to_file)
    print(file_contents)
    word_count(file_contents)

def get_book(path):
    with open(path) as f:
        return(f.read())
    
def word_count(book):
    words = book.split()
    print(len(words))

main()