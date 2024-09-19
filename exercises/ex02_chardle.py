"""EX02 - Chardle - A cute step toward Wordle."""

__author__ = "730812817"


def input_word() -> str:
    # Asks the user to input a 5-letter word
    user_word: str = input("Enter a 5-character word: ")
    # if input isn't 5 chars long, then error and exit
    if len(user_word) != 5:
        print("Error: Word must contain 5 characters.")
        exit()
    # returning the inputted word
    return user_word


def input_letter() -> str:
    # Asks the user for a single chracter
    user_letter: str = input("Enter a single character: ")
    # Checks if it is a single char, error & exits if not
    if len(user_letter) != 1:
        print("Error: Character must be a single character.")
        exit()
    # returns the letter
    return user_letter


# Checks if the user's letter is in the user's word
def contains_char(word: str, letter: str) -> None:
    # used to count the amount of times the letter appears in the word
    count: int = 0
    print("Searching for", letter, "in", word)
    # Checks all indices for a match, increments count by 1 if there is
    if word[0] == letter:
        print(letter + " found at index 0")
        count += 1
    if word[1] == letter:
        print(letter + " found at index 1")
        count += 1
    if word[2] == letter:
        print(letter + " found at index 2")
        count += 1
    if word[3] == letter:
        print(letter + " found at index 3")
        count += 1
    if word[4] == letter:
        print(letter + " found at index 4")
        count += 1

    # Displays a message based on how many instances of the user's letter is found
    if count == 1:
        print("1 instance of " + letter + " found in " + word)
    elif count > 1:
        print(count, "instances of " + letter + " found in " + word)
    else:
        print("No instances of " + letter + " found in " + word)


# Main function
def main() -> None:
    contains_char(word=input_word(), letter=input_letter())


# Allows ex02_chardle to be a module
if __name__ == "__main__":
    main()
