#program to check the guessed letter, either it is in random generated word or not

import random

word_list=["Apple","Orange","Mango"]
chosen_word=random.choice(word_list).lower()
#print(chosen_word)

lives=6
#display list
display=[]
for _ in range(len(chosen_word)):
    display+="_"
print(display)

end_of_game=False
while not end_of_game:
    #user guess
    guess=input("Guess a letter\n")

    #replacing "_" with the letters
    for position in range(len(chosen_word)):
        letter=chosen_word[position]
        if letter in guess:
            display[position]=letter

    if guess not in chosen_word:
        lives-=1
        if lives==0:
            end_of_game=True
            print("ou loose")
    #displaying final result
    print(display)

    if "_" not in display:
        end_of_game=True
        print("You win")