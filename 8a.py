import os
path = os.walk("C:\Users\User\OneDrive\Desktop")
total_files = 0
total_sub = 0
for root ,sub, files in path:
    print("root :",root)
    print("subdirectiers :", sub)
    print("files :", files)
    total_files+=len(files)
    total_sub+=len(sub)
print("total files :", total_files)
print("total Subdirectiories :", total_sub)
