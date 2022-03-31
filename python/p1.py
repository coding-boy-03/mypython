num = input("Enter the number\n")
while len(num)>1 :
    sum = 0
    for i in num:
        sum+=int(i)
    num = str(sum)
if int(num)==1:
    print("The given number is a magic Number")
else:
    print(sum)
    print("Not a magic number")
