s = input("enter the string\n")
words = s.split()
for word in words:
    print(word, ":" , len(word))
print("total Number of  words ",len(words))
