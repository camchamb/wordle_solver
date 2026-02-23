from WordleGame import *
import random

def play_wordle():
    game = WordleGame()

    while not game.is_over:
        print(f"Attempts left: {game.max_attempts - len(game.guesses)}")

        guess = input("\nEnter your guess: ").strip().lower()

        try:
            game.make_guess(guess)
        except ValueError as e:
            print(e)
            continue

    if game.is_won:
        print("🎉 Congratulations! You guessed the word!")
    else:
        print(f"😢 Game over! The word was: {game.target_word}")

# Run the game
if __name__ == "__main__":
    play_wordle()