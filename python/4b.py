from tracemalloc import start


s = input("Enter the string of email id's separated with ; : \n")
start = 0
end = s.find(";")
while end != -1:
    print(s[start:end])
    start = end+1
    end = s.find(";", start)
print(s[start::])


