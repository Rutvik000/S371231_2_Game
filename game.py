''' import random'''
import random


class GuessTheNumber:
    """
    A class for playing the Guess The Number game.
    """
    def __init__(self):
        self.random_number = self.generate_random_number()
        self.attempts = 0

    def generate_random_number(self):
        """
        Generates a random 4-digit number as the target.
        """
        random_4_digit_number = str(random.randint(1000, 9999))
        return random_4_digit_number

    def check_guess(self, guess):
        """
        Checks the user's guess and provides feedback.
        """
        self.attempts += 1
        secret_digits = [str(digit) for digit in str(self.random_number)]
        guess_digits = [str(digit) for digit in str(guess)]
        feedback = ""

        for i in range(4):
            if guess_digits[i] == secret_digits[i]:
                feedback += "0"
            elif guess_digits[i] in secret_digits:
                feedback += "X"
            else:
                feedback += "-"

        return feedback


if __name__ == '__main__':
    game = GuessTheNumber()
    print("Welcome to the game!")

    while True:

        print("Enter your 4-digit guess ():")
        print("or if you want to exit the game, type 'quit'")
        guess_digit = input()

        if guess_digit == 'quit':
            print("THE END! Have a good day.")
            break

        if len(guess_digit) != 4 or not guess_digit.isdigit():
            print("Please enter a valid 4-digit number.")
            continue

        FEEDBACK = game.check_guess(guess_digit)

        if FEEDBACK == "0000":
            print(FEEDBACK)
            print("Congratulations! You guessed the correct number")
            print(f"Your total attempts = {game.attempts} ")
            print("Do you want to play again? Press 1: Yes\nPress 2: No ")
            play_again = input()
            if play_again.lower() == '2':
                print("THE END! Have a good day.")
                break
            game = GuessTheNumber()
        else:
            print("Suggestion:", FEEDBACK)
