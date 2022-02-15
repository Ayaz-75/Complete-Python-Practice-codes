

#program to check the guessed letter, either it is in random generated word or not

import random

stages = ['''

  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
 
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
      |
      |
      |
      |
========= ''']

end_of_game=False
word_list=["Apple","Orange","Mango"]
chosen_word=random.choice(word_list).lower()



lives=6
#display list
display=[]
for _ in range(len(chosen_word)):
    display+="_"

while not end_of_game:
    #user guess
    guess=input("Guess a letter\n")

    #replacing "_" with the letters
    for position in range(len(chosen_word)):
        letter=chosen_word[position]


        if letter == guess:
            display[position]=letter

    if guess not in chosen_word:
        lives-=1
        if lives==0:
            end_of_game=True
            print("you loose")
    #displaying final result
    

    print(f"{' '.join(display)}")


    if "_" not in display:
        end_of_game=True
        print("You win")
    
    
    
    print(stages[lives])