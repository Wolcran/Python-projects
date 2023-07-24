rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

lizard = '''
              ____...---...___
___.....---"""        .       ""--..____
     .                  .            .
 .             _.--._       /|
        .    .'()..()`.    / /
            ( `-.__.-' )  ( (    .
   .         \        /    \ \ 
       .      \      /      ) )        .
            .' -.__.- `.-.-'_.'
 .        .'  /-____-\  `.-'       .
          \  /-.____.-\  /-.
           \ \`-.__.-'/ /\|\|           .
          .'  `.    .'  `.
          |/\/\|    |/\/\|
'''

spock = '''
         ⢀⣀⡀⢸⣿⣷⠀⠀⠀⠀⠀⠀⣠⣄⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣧⠈⣿⣿⡆⠀⠀⠀⠀⣼⣿⣿⠀⣤⡀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⡀⢹⣿⣧⠀⠀⠀⣸⣿⣿⠃⣰⣿⣿⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⣇⠘⣿⣿⡄⠀⢀⣿⣿⡏⢠⣿⣿⡏⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⣿⡀⢻⣿⣧⠀⣸⣿⡟⢀⣾⣿⡿⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣇⣸⣿⣿⣶⣿⣿⠁⣼⣿⣿⠁⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢀⣀⣀⣀⠀⠀⠀⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠙⢿⣿⣿⣷⣦⣀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠛⠛⠛⠛⠛⠛⠛⠃
'''

import random
player = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors, 3 for Lizard, 4 for Spock\n"))
rps = (rock, paper, scissors, lizard, spock)
computer = random.randint (0, len(rps)-1)

if 5> player >= 0:
    if player == 0:
        print (rock)
    elif player == 1:
        print (paper)
    elif player == 2:
        print (scissors)
    elif player == 3:
        print (lizard)
    elif player == 4:
        print (spock)
    print ("Computer chose:")
    if computer == 0:
        print (rock)
    elif computer == 1:
        print (paper)
    elif computer == 2:
        print (scissors)
    elif computer == 3:
        print (lizard)
    elif computer == 4:
        print (spock)
else:
    print ("Please select a valid option")

if player == computer:
    print ("It's a tie!")
if player == 0:
    if computer ==1:
        print ("Paper beats rock. You lose!")
    elif computer ==2:
        print ("Rock beats Scissors. You win!")
    elif computer ==3:
        print ("Rock crushes lizard. You win!")
    elif computer ==4:
        print ("Spock vaporizes rock. You lose!")
if player == 1:
    if computer ==0:
        print ("Paper beats rock. You win!")
    elif computer ==2:
        print ("Scissors beats paper. You lose!")
    elif computer ==3:
        print ("Lizard eats paper. You lose!")
    elif computer ==4:
        print ("Paper disproves Spock. You win!")
if player == 2:
    if computer ==0:
        print ("Rock beats Scissors. You lose!")
    elif computer ==1:
        print ("Scissors beats paper. You win!")
    elif computer ==3:
        print ("Scissors decapitates lizard. You win!")
    elif computer ==4:
        print ("Spock smashes scissors. You lose!")
if player == 3:
    if computer ==0:
        print ("Rock crushes lizard. You lose!")
    elif computer ==1:
        print ("Lizard eats paper. You win!")
    elif computer ==2:
        print ("Scissor decapitates lizard. You lose!")
    elif computer ==4:
        print ("Lizard poisons Spock. You win!")
if player == 4:
    if computer ==0:
        print ("Spock vaporizes rock. You win!")
    elif computer ==1:
        print ("Paper disproves Spock. You lose!")
    elif computer ==2:
        print ("Spock smashes scissors. You win!")
    elif computer ==3:
        print ("Lizard poisons Spock. You lose!")

