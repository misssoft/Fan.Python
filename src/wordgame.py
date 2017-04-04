import random

def get_random_word():
    words = ["Tokyo","Paris","Shanghai","London","Sydney"]
    randomnum = random.randint(0, len(words)-1)
    word = words[randomnum]
    return word

def show_blank_word(word):
    for w in word:
        print("_"," ", end="")
    print("")

def get_guess():
    print("Enter a letter:", end="")
    return input()

def process_word(letter, word):
    for w in word:
        if (letter == w):
            return True

def play_word_game():
    word = get_random_word()
    show_blank_word(word)
    guess = get_guess()
    wordIsIn = process_word(guess,word)
    
print("Guess a word")
play_word_game()
print("Game over")
