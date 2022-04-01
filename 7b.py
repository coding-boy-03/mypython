
import re
password = input("enter the text\n")
pattern = "^(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9])(?=.*[$#@_])[A-Za-z0-9$#@_]{6-16}$"

result = re.match(pattern,password)
if result:
    print("valid password", password)

