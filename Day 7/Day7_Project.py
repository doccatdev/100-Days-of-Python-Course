import random
import hangman_game
from art import stages
from art import logo

end_of_game = False

# Create a variable 'lives' to keep track of remaining lives.
lives = 6
print(logo)
print('Welcome to Hangman Game (Indonesian Words)')
print('******************************************************************************************************************')
# Randomize the word list and choose a random word
selected_words = random.choice(hangman_game.word_list)

# Create a list of underscores based on the length of the selected word
blank_letters = ["_"] * len(selected_words)  # This will generate a list of "_" of the same length as the selected word

# Print the initial blank underscores (space-separated)
print(" ".join(blank_letters))  # Joining the list with spaces for better display

corrected_letters = []

while not end_of_game:
    if lives == 0:  # Stop the game if lives are 0
        print("You lose. The word was:", selected_words)
        break  # Exit the loop
    
    guess = input('Guess a Letter: ').lower()

    # Check if guess is correct and update blank_letters
    if guess in selected_words:
        # Update blank_letters with the correct guess
        for i in range(len(selected_words)):
            if selected_words[i] == guess:
                blank_letters[i] = guess  # Update the blank_letters list with the correct guess
    else:
        if guess not in corrected_letters:  # Ensure the incorrect letter is only counted once
            corrected_letters.append(guess)
            lives -= 1
            print(f"Incorrect guess. You have {lives} lives left.")
            print(stages[lives])  # Display hangman based on lives
    
    # Print the current state of the word (with underscores or guessed letters)
    print(" ".join(blank_letters))  # Joining the list with spaces for better display
    
    # Check if the player has guessed the word correctly
    if "_" not in blank_letters:
        end_of_game = True
        print("You win! The word was:", selected_words)

    # Check if the player has lost all their lives
    if lives == 0:
        end_of_game = True
        print("You lose. The word was:", selected_words)
