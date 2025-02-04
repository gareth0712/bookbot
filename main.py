book_path = "books/frankenstein.txt"
letters = 'abcdefghijklmnopqrstuvwxyz'

def get_word_count(string):
    words = string.split()
    return len(words)

def get_char_dict(string):
    dict = {}
    string = string.lower()
    for c in list(string):
        if c not in dict:
            dict[c] = 1
        else:
            dict[c] += 1
    return dict

def sort_on(dict):
    return dict["num"]

def gen_char_list(char_dict):
    char_list = []
    for char in char_dict:
        if char not in letters:
            continue
        char_list.append({
            "name": char,
            "num": char_dict[char]
        })
    char_list.sort(reverse=True, key=sort_on)
    return char_list

def print_report(word_count, char_list):
    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} words found in the document\n")

    for char in char_list:
        print(f"The '{char["name"]}' character was found {char["num"]} times")
    print(f"--- End report ---")

def main():
    with open(book_path) as f:        
        file_contents = f.read()
        word_count = get_word_count(file_contents)
        char_dict = get_char_dict(file_contents)
        char_list = gen_char_list(char_dict)
        print_report(word_count, char_list)

main()