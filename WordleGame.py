import os

class WordleGame:
    def __init__(self, target_word: str, max_attempts: int = 6):
        self.target_word = target_word.lower()
        self.max_attempts = max_attempts
        self.guesses = []          # list of guessed words
        self.feedback = []         # list of feedback lists (G, Y, B)
        self.is_won = False
        self.is_over = False

    def make_guess(self, guess: str):
        if self.is_over:
            raise ValueError("Game is already over.")

        guess = guess.lower()

        if len(guess) != len(self.target_word):
            raise ValueError("Guess must be same length as target word.")

        if len(self.guesses) >= self.max_attempts:
            raise ValueError("No attempts remaining.")

        result = self._generate_feedback(guess)

        self.guesses.append(guess)
        self.feedback.append(result)

        if guess == self.target_word:
            self.is_won = True
            self.is_over = True
        elif len(self.guesses) == self.max_attempts:
            self.is_over = True

        self.display_colored_guess()

    def _generate_feedback(self, guess: str):
        """
        Returns a list of tuples:
        (letter, status)

        G = correct letter, correct position
        Y = correct letter, wrong position
        B = letter not in word
        """
        result = ["B"] * len(guess)
        target_chars = list(self.target_word)

        # First pass: correct position
        for i in range(len(guess)):
            if guess[i] == target_chars[i]:
                result[i] = "G"
                target_chars[i] = None  # mark as used

        # Second pass: correct letter wrong position
        for i in range(len(guess)):
            if result[i] == "B" and guess[i] in target_chars:
                result[i] = "Y"
                target_chars[target_chars.index(guess[i])] = None

        # Convert to list of tuples
        return [(guess[i], result[i]) for i in range(len(guess))]

    def remaining_attempts(self):
        return self.max_attempts - len(self.guesses)

    def get_game_state(self):
        return {
            "target_word": self.target_word if self.is_over else None,
            "guesses": self.guesses,
            "feedback": self.feedback,
            "is_won": self.is_won,
            "is_over": self.is_over,
            "remaining_attempts": self.remaining_attempts()
        }

    def display_colored_guess(self):
        """
        letter_results: list of tuples like [("C", "G"), ("R", "Y"), ...]
        G = green
        Y = yellow
        B = gray
        """
        if os.name == 'nt':
            os.system('cls')
        # For macOS/Linux
        else:
            os.system('clear')

        COLOR_MAP = {
            "G": "\033[92m",  # green
            "Y": "\033[93m",  # yellow
            "B": "\033[90m",  # gray
        }

        RESET = "\033[0m"

        for guess in self.feedback:
            for letter, status in guess:
                color = COLOR_MAP.get(status, RESET)
                print(f"{color}{letter}{RESET}", end=" ")
            print("")

        print()



# game = WordleGame("crane", 6)
# game.make_guess("miaen")
# game.make_guess("neman")
# game.make_guess("crane")
# print(game.feedback)