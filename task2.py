import random

# Reversed
oldwords = [word[::-1].split() for word in open('words.txt')]
words = oldwords[0]
randomPhrase = " ".join([words[random.randrange(0, len(words))] for i in range(4)])

randomPhraseList = randomPhrase.split(' ')
reverserandomList = randomPhraseList[::-1]

print(randomPhrase)
print(randomPhraseList)
print(reverserandomList)