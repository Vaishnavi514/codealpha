import random

def select_word():
    words = ["hangman", "python", "programming", "codealpha", "internship", "challenge", "Tasks"]
    return random.choice(words)

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

def hangman():
    max_limit = 6
    guessed_letters = []
    word_to_guess = select_word()
    attempts = 0

    print("Welcome to Hangman!")
    
    while True:
        print("\nCurrent word: " + display_word(word_to_guess, guessed_letters))
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter. Try again.")
            continue

        guessed_letters.append(guess)

        if guess not in word_to_guess:
            attempts += 1
            print("Incorrect guess. Attempts left: {}".format(max_limit - attempts))
            if attempts == max_limit:
                print("Game over! The word was: {}".format(word_to_guess))
                break
        else:
            print("Good guess!")

        if set(guessed_letters) >= set(word_to_guess):
            print("Congratulations! You've guessed the word: {}".format(word_to_guess))
            break

if __name__ == "__main__":
    hangman()
