def main():
    book_path = "books/frankenstein.txt"
    print_report(book_path)


def print_report(path):
    print(f"--- Begin report of {path} ---")
    contents = get_book_contents(path)
    num_words = get_num_words(contents)
    character_counts = sort_character_counts(get_character_counts(contents))
    print(f"{num_words} found in the document")
    print()
    for char, count in character_counts.items():
        print(f"The '{char}' character was found {count} times")
    print("--- End report ---")


def get_book_contents(path):
    with open(path, "r") as f:
        file_contents = f.read()
        return file_contents


def get_num_words(text):
    return len(text.split())


def get_character_counts(text):
    counts = {}
    for char in text:
        if not char.isalnum():
            continue
        char = char.lower()
        counts[char] = 1 + counts[char] if char in counts else 1
    return counts


def sort_character_counts(counts):
    unsorted_items = counts.items()
    sorted_items = sorted(
        unsorted_items, key=lambda item: item[1], reverse=True)
    return dict(sorted_items)


if __name__ == "__main__":
    main()
