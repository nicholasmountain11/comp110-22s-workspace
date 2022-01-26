"""Exercise 2, one shot wordle."""

__author__ = 730477365

secret_word: str = "python"
letter_count: int = len(secret_word)
word_guess: str = input(f"What is your {letter_count}-letter guess? ")

while len(word_guess) != letter_count:
    word_guess = input(f"That was not {letter_count} letters! Try again: ")

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

i: int = 0
box_string: str = ""


while i < letter_count:
    if secret_word[i] == word_guess[i]:
        box_string = f"{box_string}{GREEN_BOX}"
    else:
        guessed_exists: bool = False
        alt_index: int = 0
        while not guessed_exists and alt_index < letter_count:
            if secret_word[alt_index] == word_guess[i]:
                guessed_exists = True
            else:
                alt_index = alt_index + 1
        if guessed_exists:
            box_string = f"{box_string}{YELLOW_BOX}"
        else:
            box_string = f"{box_string}{WHITE_BOX}"
    i = i + 1


print(box_string)
if word_guess == secret_word:
    print("Woo! you got it!")
else:
    print("Not quite. Play again soon!")