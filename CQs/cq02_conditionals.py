"""A simple number guessing game."""

__author__ = "730812817"


def guess_a_number() -> None:
    secret: int = 7
    number_guessed: int = int(input("Guess a number: "))
    print("Your guess was", number_guessed)
    if number_guessed == secret:
        print("You got it!")
    elif number_guessed < secret:
        print("Your guess was too low! The secret number is", secret)
    else:
        print("Your guess was too high! The secret number is", secret)


if __name__ == "__main__":
    guess_a_number()
