import random

# List of predefined words
words = ["python", "coding", "alpha", "intern", "program"]

# Random word selection
word = random.choice(words)
guessed_letters = []
wrong_guesses = 0
max_wrong = 6

print(" Welcome to Hangman Game!")
print("Guess the word letter by letter.")
print("_ " * len(word))

while wrong_guesses < max_wrong:
    guess = input("\nEnter a letter: ").lower()

    if guess in guessed_letters:
        print(" You already guessed this letter.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print(" Correct guess!")
    else:
        wrong_guesses += 1
        print(f" Wrong guess! Attempts left: {max_wrong - wrong_guesses}")

    # Display word progress
    display_word = ""
    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print(display_word)

    # Win condition
    if "_" not in display_word:
        print(" Congratulations! You guessed the word correctly!")
        break

# Lose condition
if wrong_guesses == max_wrong:
    print("\n Game Over!")
    print("The word was:", word)
