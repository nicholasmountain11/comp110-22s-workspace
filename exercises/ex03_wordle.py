"""Making wordle with multiple guesses allowed."""

__author__ = "730477365"


def contains_char(secret_word: str, letter_guess: str) -> bool:
    """Decides if the secret word includes a given letter."""
    assert len(letter_guess) == 1
    i: int = 0
    guessed_exists: bool = False
    while not guessed_exists and i < len(secret_word):
        if secret_word[i] == letter_guess:
            guessed_exists = True
            return True
        i += 1
    return False 


WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


def emojified(word_guess: str, word_secret: str) -> str:
    """Uses emojis to tell the user how correct their guess was."""
    assert len(word_guess) == len(word_secret) 
    letter_index: int = 0
    box_string: str = ""
    while letter_index < len(word_secret):
        if word_guess[letter_index] == word_secret[letter_index]:
            box_string = f"{box_string}{GREEN_BOX}"
        elif contains_char(word_secret, word_guess[letter_index]):
            box_string = f"{box_string}{YELLOW_BOX}"
        else:
            box_string = f"{box_string}{WHITE_BOX}"
        letter_index += 1
    return f"{box_string}"


def input_guess(expected_length: int) -> str:
    """Makes sure the user's guess is the correct number of characters."""
    guess_new = input(f"Enter a {expected_length} character word: ")
    guess_length: int = len(guess_new)
    while guess_length != expected_length:
        guess_new = input(f"That wasn't {expected_length} chars! Try again: ")
        guess_length = len(guess_new)
    return f"{guess_new}"


def main() -> None:
    """The entry point of the program and main game loop."""
    word: str = "codes"
    turns: int = 1
    correct_guess: bool = False
    while not correct_guess and turns < 7:
        print(f"=== Turn {turns}/6 ===")
        user_guess: str = input_guess(len(word))
        if user_guess == word:
            print(f"{emojified(user_guess, word)} \nYou won in {turns}/6 turns!")
            correct_guess = True
        else:
            print(emojified(user_guess, word))
        turns += 1
    if turns == 7:
        print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main()