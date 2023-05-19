import random

DICTIONARY_FILE = "five_letter_words.txt"

ANSI_RESET = "\u001B[0m"
GREEN = "\u001B[42m"
YELLOW = "\u001B[43m"
WHITE = "\u001B[47m"

GuessesLeft = 0
dictionary = []

def get_word():
    random.seed()
    with open(DICTIONARY_FILE) as file:
        words = file.read().split()
    word = random.choice(words).lower()
    return list(word)

def input(word):
    return list(word)

def exists(guess):
    global GuessesLeft
    if guess not in dictionary:
        print("This word does not exist in our dictionary.")
        return False
    else:
        GuessesLeft -= 1
        return True

def play_game(answer):
    guess = input().lower()
    if exists(guess):
        word = input(guess)
        for i in range(len(word)):
            if word[i] == answer[i]:
                print(GREEN + word[i] + ANSI_RESET, end='')
            elif word[i] in answer:
                print(YELLOW + word[i] + ANSI_RESET, end='')
            else:
                print(WHITE + word[i] + ANSI_RESET, end='')
        print()
        if word == answer:
            global GuessesLeft
            GuessesLeft = 0
            print("Good job!")

print("\n \nWelcome to Wordle!" + 
      "\nThe object of the game is to guess the given 5 letter word in six attempts or less." +
      "\nIf the letter is found within the word and in the correct position, it will print in " + GREEN + "green." + ANSI_RESET +
      "\nIf the letter is found within the word but not in the correct position, it will print in " + YELLOW + "yellow." + ANSI_RESET +
      "\nIf the letter is not present in the word at all, it will print in " + WHITE + "white." + ANSI_RESET +
      "\n \nBegin by guessing any 5 letter word below.\n")

with open(DICTIONARY_FILE) as file:
    dictionary = [word.lower() for word in file.read().split()]

answer = get_word()
GuessesLeft = 6

while GuessesLeft > 0:
    play_game(answer)

if GuessesLeft == 0:
    print("The correct word was ", end='')
    for letter in answer:
        print(WHITE + letter + ANSI_RESET, end='')
    print(".")

