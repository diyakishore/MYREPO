import random

def choose_word():
    words = ["python", "hangman", "programming", "computer", "coding", "developer"]
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
    word_to_guess = choose_word()
    guessed_letters = []
    attempts = 6

    print("Welcome to Hangman!")
    
    while attempts > 0:
        print("\nAttempts left:", attempts)
        current_display = display_word(word_to_guess, guessed_letters)
        print("Current word:", current_display)

        guess = input("Enter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter. Try again.")
            continue

        guessed_letters.append(guess)

        if guess not in word_to_guess:
            attempts -= 1
            print("Incorrect guess!")

        if set(word_to_guess) == set(guessed_letters):
            print("\nCongratulations! You guessed the word:", word_to_guess)
            break

    if attempts == 0:
        print("\nSorry, you ran out of attempts. The word was:", word_to_guess)

if __name__ == "__main__":
    hangman()
    #This is a basic implementation, and you can modify and extend it as needed. The game randomly selects a word from a predefined list, and the player has to guess the word one letter at a time. The player has 6 attempts to guess the word correctly. You can customize the list of words or add more features to make the game more interesting.
