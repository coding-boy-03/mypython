import random
objects = ["rock","paper","scissor"]
while True:
    sys_ch = random.choice(objects)
    user_ch = input("enter your choice\n")
    print("system choice :" , sys_ch)

    if sys_ch == user_ch:
        print("it is draw")
    elif sys_ch == "rock":
        if user_ch == "paper":
            print("The user wins")
        elif user_ch == "scissor" :
            print("System wins")
    elif sys_ch == "paper":
        if user_ch == "scissor":
            print("user wins")
        elif user_ch == "rock":
            print("system wins")
    elif sys_ch == "scissor":
        if user_ch == "rock":
            print("user wins")
        elif user_ch == "paper":
            print("system wins")
    if user_ch not in objects:
        print("invalid choice")
        break

