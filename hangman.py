import random
hang=[
"""
----+
|   |
    |
    |
    |
    |
=========
""",
""""
----+
|   |
O   |
    |
    |
    |
=========
"""
,
"""
----+
|   |
O   |
|   |
    |
    |
=========
"""
,

"""    
-----+
 |   |
 O   |
/|   |
     |
     |
=========
""",
"""    
-----+
 |   |
 O   |
/|\\  |
     |
     |
=========
""",
"""    
-----+
 |   |
 O   |
/|\\  |
/    |
     |
=========
""",
"""    
-----+
 |   |
 O   |
/|\\  |
/ \\  |
     |
=========
"""]
with open("english.txt","r") as f:
    words = f.read().splitlines()

def hangman():
    secret_word = random.choice(words)
    guessed_letters = set()
    attempts=6

    print("Welcome to Hangman!")
    while attempts > 0:
        print(hang[6-attempts])
        display=" "
        for letter in secret_word:
            if letter in guessed_letters:
                display+=letter+" "
            else:
                display+="_"

        print("\n words",display)
        print("Remaining attempts: ",attempts)
        if all(letter in guessed_letters for letter in secret_word):
            print("You win!")
            return

        guess=input("Guess a letter: ").lower().strip()

        if len(guess)!=1 or not guess.isalpha():
            print("Please enter a letter only")
            continue

        if guess in guessed_letters:
            print("You already guessed this letter")
            continue

        guessed_letters.add(guess)

        if guess in secret_word:
            print("You guessed this letter")
        else:
            print("Sorry, that letter was not in the word")
            attempts-=1
    print(hang[6])
    print("Game Over")
    print("The word was",secret_word)

hangman()


