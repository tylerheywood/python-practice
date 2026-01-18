
string = input("Please enter a string: ").upper()
words = string.split()
words_unique = {}

for word in words:
    words_unique[word] = words_unique.get(word, 0) + 1

for word in words_unique:
    print(word," -> ",words_unique[word])
