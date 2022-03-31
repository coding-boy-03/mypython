from unittest import result


s = input(" enter the string\n")
words = s.split()
result = " "
for word in words:
    if word.lower() != "the":
        result+=word+" "
print(result)

