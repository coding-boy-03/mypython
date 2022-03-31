n = int(input("enter the specified number of printing prime number\n"))
for i in range(2,n+1):
    prime = True
    for j in range(2,i):
        if i%j == 0:
            prime=False
    if prime == True:
        print(i)
