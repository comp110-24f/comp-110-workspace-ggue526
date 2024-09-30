"""Wordle Recreation."""

__author__ = "730812817"


def input_guess(word_length: int) -> str:
    # Prompts user for a guess
    user_guess: str = input(f"Enter a {word_length} character word: ")
    # Error until user_guess is correct length
    while len(user_guess) != word_length:
        user_guess = input(f"That wasn't {word_length} chars! Try again: ")
    return user_guess


def contains_char(word: str, letter: str) -> bool:
    """Searches word for letter, returns True if letter is found"""
    # asserts 1 letter
    assert len(letter) == 1
    count = 0
    while count < len(word):
        # Checks all of word (which is secret) to see if it has letter.
        if word[count] == letter:
            return True
        # inc prog
        count += 1
    return False


def emojified(guess: str, secret: str) -> str:
    """Compares the two strings and 'emojifies' the output"""

    # makes sure guess and secret are the same length
    assert len(guess) == len(secret)

    # Constants :DD
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"

    # I decided to just concatenate to an empty string bc it seemed easier
    result: str = ""

    # for indexing
    count: int = 0

    # compares all indices against secret
    while count < len(guess):
        # Green if the same
        if guess[count] == secret[count]:
            result += GREEN_BOX
        # Yellow if present
        elif contains_char(secret, guess[count]):
            result += YELLOW_BOX
        # white if none
        else:
            result += WHITE_BOX
        # inc prog
        count += 1
    return result


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""
    # counts the rounds for the header
    round: int = 1
    # makes sure there are 6 rounds
    while round < 7:
        # displays current round
        print(f"=== Turn {round}/6 ===")
        # takes the users guess and stores it
        current_guess: str = emojified(input_guess(len(secret)), secret)
        # so i can print it's output
        print(current_guess)
        # and see if they've got it right
        if current_guess == ("\U0001F7E9" * len(secret)):
            print(f"You won in {round}/6 turns!")
            # can't forget to exit :D
            exit()
        # inc prog
        round += 1
    print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main(secret="codes")
