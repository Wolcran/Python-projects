import random
from hangman_art import stages
from hangman_words import word_list
from hangman_art import logo
# from replit import clear

print (logo)

end_of_game = False

chosen_word = random.choice(word_list)
word_length = len(chosen_word)
lives = 6
guess_list=[]

# print(f'Pssst, the solution is {chosen_word}.')

display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    for position in range(word_length):
        letter = chosen_word[position]
# Used for building
# print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter
    print(f"{' '.join(display)}")

    if guess not in chosen_word and guess not in guess_list:
        print (f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            end_of_game=True
            print("You lose.")

    guess_list += guess
    count = guess_list.count(guess)
    if count == 1 and guess in display:
            print(f"You guessed {guess} correctly, good job! :)")
    if count >= 2:
        print("You have already guessed this letter.")



    if "_" not in display:
        end_of_game = True
        print("You win.")
    print (stages[lives])

