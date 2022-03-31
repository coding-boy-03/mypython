s = input("enter the string present between @ and #\n")
index1 = s.find("@")
index2 = s.find("#",index1)
print(s[index1+1:index2])