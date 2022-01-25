"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730477365"

word_guess: str = input("Enter a 5-character word: ")
if len(word_guess) != 5:
    print("Error: Word must contain 5 characters")
    exit()

letter_guess: str = input("Enter a single character: ")
if len(letter_guess) != 1:
    print("Error: Character must be a single character")
    exit()

letter_instances: int = 0

print("Searching for " + letter_guess + " in " + word_guess)

if letter_guess == word_guess[0]:
    print(letter_guess + " found at index 0")
    letter_instances = letter_instances + 1

if letter_guess == word_guess[1]:
    print(letter_guess + " found at index 1")
    letter_instances = letter_instances + 1

if letter_guess == word_guess[2]:
    print(letter_guess + " found at index 2")
    letter_instances = letter_instances + 1

if letter_guess == word_guess[3]:
    print(letter_guess + " found at index 3")
    letter_instances = letter_instances + 1

if letter_guess == word_guess[4]:
    print(letter_guess + " found at index 4")
    letter_instances = letter_instances + 1

if letter_instances < 1:
    print("No instances of " + letter_guess + " found in " + word_guess)
else:
    if letter_instances == 1:
        print("1 instance of " + letter_guess + " found in " + word_guess)
    else: 
        print(str(letter_instances) + " instances of " + letter_guess + " found in " + word_guess)