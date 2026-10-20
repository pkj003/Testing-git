from dataclasses import dataclass


@dataclass(frozen=True)
class Difficulty:
    max_number: int
    attempts: int


DIFFICULTIES = {
    "1": ("Easy", Difficulty(max_number=50, attempts=10)),
    "2": ("Medium", Difficulty(max_number=100, attempts=7)),
    "3": ("Hard", Difficulty(max_number=200, attempts=6)),
}


def choose_difficulty() -> Difficulty:
    print("\nChoose a difficulty:")
    for option, (name, settings) in DIFFICULTIES.items():
        print(f"{option}. {name} (1-{settings.max_number}, {settings.attempts} guesses)")

    while True:
        choice = input("Enter 1, 2, or 3: ").strip()
        if choice in DIFFICULTIES:
            name, settings = DIFFICULTIES[choice]
            print(f"{name} difficulty selected.")
            return settings
        print("Please enter 1, 2, or 3.")
