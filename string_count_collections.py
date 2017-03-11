from collections import Counter

"""
Declaring and Counting String Length, Number of Words in String
using Module collections
"""

sentence = "the cat sat on the mat with the rat cat and rat were playing in the mat and the cat was happy with rat on the mat"

print("Sentence is: ",sentence)
print("Length of sentence:", len(sentence))
print("Numbe of Occurrences of 'cat': ", sentence.count('cat'))

#Split sentence, generating List
words = sentence.split()
print("Words ", words)
print("Type Words: ",type(words))

#using Counter
counts = Counter(words)
print("\nType counts: ",type(counts))
print(counts)

print("\n Occurrences of 'cat': ",counts['cat'])