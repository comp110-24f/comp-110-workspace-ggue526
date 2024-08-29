"""Plan the coziest tea party!"""

# My PID :3
__author__: str = "730812817"


# Gathers all the functions together
def main_planner(guests: int) -> None:
    """The entry point of the program"""
    print("A Cozy Tea Party for " + str(guests) + " people!")
    print("Tea Bags: " + str(tea_bags(guests)))
    print("Treats: " + str(treats(guests)))
    print("Cost: $" + str(cost(tea_bags(guests), treats(guests))))


def tea_bags(people: int) -> int:
    """Calculates the amount of tea bags needed depending on the amount of guests"""
    # multiplies the argument by 2
    return people * 2


def treats(people: int) -> int:
    """Calculates the amount of treats depending on the amount of guests"""
    # takes the result of tea_bags(people) and multiplies it by 1.5
    return int(tea_bags(people=people) * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """Calculates a cost for the amount of tea bags and treats needed"""
    # Assuming tea bags are $0.50 and treats are $0.75
    return (tea_count * 0.50) + (treat_count * 0.75)


# Have to place below functions because they haven't been defined yet at the top of the program
if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
