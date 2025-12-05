#Hangman game in python

import random
from wordslist import words

hangman_art = {0: ("   ",
                   "   ",
                   "   "),
               1: (" o ",
                   "   ",
                   "   "),
               2: (" 0 ",
                   " | ",
                   "   "),
               3: (" o ",
                   "/| ",
                   "   "),
               4: (" o ",
                   "/|\\",
                   "   "),
               5: (" o ",
                   "/|\\",
                   "/  "),
               6: (" o ",
                   "/|\\",
                   "/ \\")}

#__________Display the Hangman__________
def display_man(wrong_guesses):
    print("***************")
    for line in hangman_art[wrong_guesses]:
        print(line)
    print("***************")

#__________Display the hint__________
def diaplay_hint(hint):
    print(" ".join(hint))

#__________Display the final answer__________
def display_answer(answer):
    print(" ".join(answer))

#__________Main function__________
def main():
    answer = random.choice(words)
    hint = ['_'] * len(answer)
    wrong_guesses = 0
    guessed_letter = set()
    is_running = True

    #Loop to keep the game running
    while is_running:
        print("___________WELCOME TO HANGMAN GAME__________")
        display_man(wrong_guesses)
        diaplay_hint(hint)
        guess = input("Enter your guess: ").lower()
        
        #Checks for any wrong inputs
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input!")
            continue
        
        #Checks for any guesses that have already beed added
        if guess in guessed_letter:
            print(f"{guess} is already guessed")
            continue

        guessed_letter.add(guess)    #Add the guess to a set for checking if the letter have be guessed later in the code

        if guess in answer:
            for i in range(len(answer)):
                if answer[i] == guess:
                    hint[i] = guess
        else:
            wrong_guesses += 1
        
        #Ends the game
        if "_" not in hint:
            display_man(wrong_guesses)
            display_answer(answer)
            print("You won!")
            is_running = False
        elif wrong_guesses >= len(hangman_art) - 1:
            display_man(wrong_guesses)
            display_answer(answer)
            print("You lose!")
            is_running = False

if __name__ == "__main__":
    main()
