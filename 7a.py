import re
s = input(" enter the text\n")
pattern = "[a-zA-Z0-9_.]+@[a-zA-Z0-9]+\.[a-zA-Z]+"
words = s.split()
for word in words:
    result = re.match(pattern,word)
    if result:
        print(word)
        
    else:
        print("invalid email id")
        print(word)
       
