from sympy import false

from WordleGame import WordleGame

class WordleSolver:
    def __init__(self):
        with open("in-freq-order.txt") as f:
            self.word_freq = [line.strip() for line in f]

    def matches_feedback(self, word, feedback):
        """
        word: candidate word
        feedback: list of tuples like [('a','B'), ('r','Y'), ('c','G')]
        Returns True if word follows the feedback rules
        """
        word = list(word.lower())
        target_letters = list(word)  # copy to track used letters

        # First check greens
        for i, (letter, status) in enumerate(feedback):
            if status == "G":
                if word[i] != letter:
                    return False
                # mark letter as used
                target_letters[i] = None

        # Then check yellows
        for i, (letter, status) in enumerate(feedback):
            if status == "Y":
                if word[i] == letter:
                    return False  # cannot be in this position
                if letter not in target_letters:
                    return False  # letter must exist elsewhere
                # mark first occurrence as used
                target_letters[target_letters.index(letter)] = None

        # Finally check blacks
        for i, (letter, status) in enumerate(feedback):
            if status == "B":
                # letter cannot appear in any remaining positions
                if letter in target_letters:
                    return False

        return True

    def does_word_match(self, word, feedback):
        for guess in feedback:
            if not self.matches_feedback(word, guess):
                return False
        return True


    def get_most_common_word(self, game: WordleGame):
        for word in self.word_freq:
            if self.does_word_match(word, game.feedback):
                return word
        return None

    def get_list_common_word(self, game: WordleGame):
        results = []
        for word in self.word_freq:
            if self.does_word_match(word, game.feedback):
                results.append(word)
        return results



# game = WordleGame("guava")
# game.make_guess("audio")
#
# while not game.is_over:
#     game.make_guess(get_most_common_word(word_freq, game))

# game = WordleGame()
# game.feedback = [[("c", "B"), ("r", "B"), ("a", "G"), ("n", "B"), ("e", "B")],
#                  [("p", "B"), ("l", "B"), ("a", "G"), ("n", "B"), ("t", "B")],
#                  [("f", "B"), ("l", "B"), ("a", "G"), ("s", "B"), ("k", "B")]]
#
#
# print(get_list_common_word(word_freq, game))