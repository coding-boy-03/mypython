from itertools import count


s = input("Enter the string\n")
count = 0
c = input("Enter the character to be counted\n")
for i in s:
    if i == c :
        count+=1
print(" the occurence of character :", c ,"in string S", count)
