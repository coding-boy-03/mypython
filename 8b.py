file1 = open("E:\new.txt")
string = file1.read()
lines = string.splitlines()
oddlines = ""
for index in range(0,len(lines),2):
    oddlines+=lines[index]+"\n"
file2 = open("E:\fresh.txt","w")
file2.write(oddlines)
file2.close()
file1.close()
print("complete")