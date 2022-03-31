from itertools import count


occ_dic = { }
s = input(" enter the string \n")

for char in s:
    if char in occ_dic.keys():
        occ_dic[char]+=1
    else :
        occ_dic[char] =1
print(occ_dic)