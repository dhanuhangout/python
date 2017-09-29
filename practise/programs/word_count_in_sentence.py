"""This module counts number of words present in a sentence."""
def word_count(sentence):
    words = sentence.split()
    return len(words)

if __name__ == '__main__':
    sentence = raw_input(
      "Enter a sentence to find number of words present in it.")
    print word_count(sentence)
