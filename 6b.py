n = int(input(" enter the Nth value of fibonacci series\n"))
l =[]
if n==1:
    l.append(0)
else:
    l.append(0)
    l.append(1)
for i in range(2,n):
    l.append(l[i-2]+l[i-1])
l.reverse()
print(l)
