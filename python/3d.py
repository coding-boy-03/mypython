guest = {
    "a" : {
        "apple" : 5,
        "banana" : 6
    } ,
    "b" : {
        "apple" : 10 ,
        "mango" : 20
    } ,
    "c" : {
        "orange" : 8,
        "watermelon" : 9
    }
}
count = 0
for x in guest.values():
    if "apple" in x.keys():
        count+=x["apple"]
print("the total number of apple :"  , count)

