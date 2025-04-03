import sys


from stats import get_num_words


def main():
    if len(sys.argv) < 2:
        print('Usage: python3 main.py <path_to_book>')
        sys.exit(1)
    book_path = sys.argv[1]
    print_report(book_path)


def print_report(path):
    print(f"--- Begin report of {path} ---")
    contents = get_book_contents(path)
    num_words = get_num_words(contents)
    character_counts = sort_character_counts(get_character_counts(contents))
    print(f"{num_words} words found in the document")
    print()
    for char, count in character_counts.items():
        print(f"{char}: {count}")
    print("--- End report ---")


def get_book_contents(path):
    with open(path, "r") as f:
        file_contents = f.read()
        return file_contents


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
