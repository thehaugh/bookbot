def main():
    text = get_book_text("./books/frankenstein.txt")
    print(count_words(text))

def count_words(text):
    return len(text.split())

def get_book_text(file_path):
    with open(file_path, "r") as f:
        return f.read()

if __name__ == "__main__":
    main()
