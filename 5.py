hint = " The fruit the keeps doctor away"
word = "apple"
turns = len(word)+1
guess = ["_"]* len(word)
print(hint)
while turns>0:
    print(guess)
    letter  = input(" enter your guess\n")
    if letter in word:
        for index in range(len(word)):
            if word[index] == letter:
                guess[index]=letter
        print("Right guess\n")
    else:
        print("Invalid chioce\n")
    turns-=1
    print("remaing NO Turns :",turns)
    if list(word) == guess :
        print(" Your guessed word is correct: ")
        break
