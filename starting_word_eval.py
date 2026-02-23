import json

from numpy.ma.extras import average

from WordleGame import *
from wordle_solver import *

with open("in-freq-order.txt") as f:
    valid_words = [line.strip() for line in f]
with open("wordle-word-bank.txt") as f:
    f.readline()
    wordle_words = [line.strip() for line in f]

results = []
solver = WordleSolver()

with open('data.json', 'r') as json_file:
    results = json.load(json_file)

print(results[:])
print("Working")
try:
    for first_guess in valid_words:
        game_length = []
        for word in wordle_words:
            game = WordleGame(word.strip(), 100)
            game_length.append(solver.play_game(first_guess.strip(), game))
        results.append((first_guess, average(game_length)))
        print(f"Finished: {first_guess}")

except KeyboardInterrupt:
    with open('data1.json', 'w') as json_file:
        json.dump(results, json_file, indent=4)

