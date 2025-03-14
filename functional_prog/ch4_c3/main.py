def find_longest_word(document: str, longest_word=""):
    words: list[str] = document.split()
    for word in words:
        if len(word) > len(longest_word):
            longest_word = word
    return longest_word
