# Rock Paper Scissors GAME
import random
print()
print()
print("-----Welcome to the Rock Paper Scissors GAME-----")
print()
rock=("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

Paper=("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

Scissors=("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")

game_images=[rock,Paper,Scissors]
user_choice=int(input("What do you choose  ?"))



if user_choice>3 or user_choice<0:
    print("You have entered an invalid number, you loose")
    
else:
    print(game_images[user_choice])
    computer_choice=random.randint(0,2)
    #print("Computer chose: ",computer_choice)
    print(game_images[computer_choice])


    if user_choice==0 and computer_choice==2:
        print("You Win")
    elif computer_choice==0 and user_choice==2:
        print("You loose")
    elif computer_choice > user_choice:
        print("You loose")
    elif user_choice>computer_choice:
        print("You win")
    elif computer_choice==user_choice:
        print("it's a draw")