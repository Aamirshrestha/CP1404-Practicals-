"""
Count word occurrences in a string
s
"""

word_to_count = {}
text = input("Text: ")
# text = "this is a collection of words of nice words this is a fun thing it is"
words = text.split()
for word in words:
    frequency = word_to_count.get(word, 0)
    word_to_count[word] = frequency + 1

# in alphabetical order
words = list(word_to_count.keys())
words.sort()

# generator function (like a list comprehension) of lengths of words
max_length = max((len(word) for word in words))
for word in words:
    print("{:{}} : {}".format(word, max_length, word_to_count[word]))