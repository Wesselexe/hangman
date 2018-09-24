"""This is a game of hangman. The goal is to guess the word by guessing each
character within the given word. The player has only a certain amount of
guesses and will only win the game, if they guess the word without guessing
the wrong characters to many time."""

import time
from random import randint

player_name = raw_input("Welcome, please enter your name: ")
print "\n"
time.sleep(1.5)

print "Welcome %s time to play hangman" % player_name
print "\n"
time.sleep(1.5)

words = ["cat", "tiger", "bird", "snail"]
secret_word = words[randint(0, len(words) - 1)]

num_guesses = len(secret_word)
tries = 5
hidden_word = []
guessed_words = []
alphabet = "abcdefghijklmnopqrstuvwxyz"

for i in range(1, len(secret_word) + 1):
    hidden_word.append(["_"])

def show_hidden_word():
    for i in hidden_word:
        print " ".join(i),

print "The category is animals, good luck!\n"
show_hidden_word()
time.sleep(1)

print "\n"

while num_guesses > 0 and tries > 0:

    guess = raw_input("Guess a character: ")
    guess = guess.lower()

    if guess in guessed_words:
        print "You already guessed that, try again.\n"

    elif guess not in alphabet:
        print "Enter a letter from a-z alphabet\n"

    elif guess in secret_word:
        guessed_words.append(guess)
        print "Correct!"
        for i in range(len(secret_word)):
            if secret_word[i] == guess:
                num_guesses -= 1
                hidden_word[i] = guess
                show_hidden_word()
                print "\n"
    else:
        tries -= 1
        print "\n"
        print "Oops, you have " + str(tries) + " tries left..."
        show_hidden_word()
        print "\n"

if num_guesses == 0:
    print "Congratulations %s! You won!! Go have some cake!!" % player_name

else:
    print "To bad, you lost. Better luck next time!"

wait = raw_input("click enter to exit")
