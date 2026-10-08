def count_words(text):
    words = text.split()
    num_words = len(words)
    num_chars = len(text)
    sentences = text.split('.')
    num_sentences = len(sentences) - 1 if text.count('.') > 0 else 1

    return num_words, num_chars, num_sentences

if __name__ == "__main__":
    text = input("enter your sentense: ")
    word_count, char_count, sentence_count = count_words(text)

    print("\nword:", word_count)
    print("letter:", char_count)
    print("sentenses:", sentence_count)