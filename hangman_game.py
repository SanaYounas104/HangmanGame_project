import random

#create list of predefined words

words = ["python","computer","programming","developer","internship"]

# Randomly select one word
word = random.choice(words)

#store the letters guess by the user

guessed_letters = []

incorrect_guesses = 0
max_incorrect_guesses = 6


hangman = [
    """
     -----
     |   |
         |
         |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
         |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
     |   |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
    /    |
    =========
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
    / \\  |
    =========
    """
]

print("Welcome to Hangman game!")
print("Guess the word one letter at a time")

while incorrect_guesses < max_incorrect_guesses:

    display_word = ""

    for letter in word:
        if letter in guessed_letters:
            display_word += letter
        else:
            display_word += "_"


    print(hangman[incorrect_guesses])
    print("\nWord:", display_word)
    # print("Incorrect guesses left:",
    #       max_incorrect_guesses - incorrect_guesses)

    #check if the player guess the complete word

    if "_" not in display_word:
        print("Congratulations! You guessed the word.", word)
        break

    # Take input from the user
    guess = input("Guess a letter:").lower()

    # Check if user only enter one letter
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one letter")
        continue

    #check if letter was already guessed
    if guess in guessed_letters:
        print("You already guess this letter")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("Correct guess!")
    else:
        incorrect_guesses += 1
        print("Wrong Guess!")
else:
         print(hangman[incorrect_guesses])
         print("\n💀 Game Over!")
         print("The word was:", word)
