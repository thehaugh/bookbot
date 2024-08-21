def main():
    print_report("./books/frankenstein.txt")

def count_words(text):
    return len(text.split())

def count_characters(text):
    character_counts = {}
    for character in text:
        lcharacter = character.lower()
        if lcharacter in character_counts:
            character_counts[lcharacter] += 1
        else:
            character_counts[lcharacter] = 1
    return character_counts

def dict_to_list_of_dict(d):
    l = []
    for k in d:
        l.append({"char": k, "num": d[k]})
    return l

def sort_on_num(d):
    return d["num"]


def print_report(book):
    text = get_book_text(book)
    word_count = count_words(text)
    character_counts = dict_to_list_of_dict(count_characters(text))
    character_counts.sort(reverse=True, key=sort_on_num)

    print(f"--- Begin report of {book}---")
    print(f"{word_count} words found in document\n")

    for character in character_counts:
        char = character["char"]
        num = character["num"]
        if character["char"].isalpha():
            print(f"The {char} character appeared {num} times.")

    print(f"--- End report of {book}---")

def get_book_text(file_path):
    with open(file_path, "r") as f:
        return f.read()

if __name__ == "__main__":
    main()
