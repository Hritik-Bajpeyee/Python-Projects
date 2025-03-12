#  Let the user guess a random number within a range.
# Provide hints like "Too High" or "Too Low.
import random

def get_attempts(difficulty):
    """Return the number of allowed attempts based on difficulty level."""
    difficulty_levels = {
        'easy': 15,
        'medium': 10,
        'hard': 5,
        'unlimited': float('inf')  # Infinite attempts for unlimited mode
    }
    if difficulty not in difficulty_levels:
        raise ValueError("Invalid difficulty level. Please enter 'easy', 'medium', 'hard', or 'unlimited'.")
    return difficulty_levels[difficulty]

def number_guessing_game():
    """Main function to play the number guessing game."""
    print("Welcome to the Number Guessing Game!")

    while True:
        # Loop until a valid difficulty is selected
        while True:
            try:
                print("\nSelect a difficulty level: Easy, Medium, Hard, Unlimited")
                difficulty = input("Enter difficulty (Easy/medium/hard/unlimited): ").lower()
                
                attempts_left = get_attempts(difficulty)
                
                if attempts_left == 15:
                    print("You selected Easy mode. You have 15 attempts.")
                elif attempts_left == 10:
                    print("You selected Medium mode. You have 10 attempts.")
                elif attempts_left == 5:
                    print("You selected Hard mode. You have 5 attempts.")
                elif attempts_left == float('inf'):
                    print("You selected Unlimited mode. You can guess as many times as you want!")
                break  # Exit the loop when a valid difficulty is selected

            except ValueError as e:
                print(f"❌ {e}")

        # Generate a random number between 1 and 100
        number_to_guess = random.randint(1, 100)
        guessed_correctly = False

        while attempts_left > 0 and not guessed_correctly:
            try:
                # Display attempts left unless in unlimited mode
                if attempts_left != float('inf'):
                    print(f"\nYou have {attempts_left} attempts left.")
                
                user_guess = int(input("Enter your guess (1-100): "))

                if user_guess < 1 or user_guess > 100:
                    print("Please enter a number between 1 and 100.")
                    continue

                if attempts_left != float('inf'):
                    attempts_left -= 1

                if user_guess < number_to_guess:
                    print("Too Low! Try again.")
                elif user_guess > number_to_guess:
                    print("Too High! Try again.")
                else:
                    guessed_correctly = True
                    print(f"\n🎉 Congratulations! You guessed the number {number_to_guess} correctly.")
            except ValueError:
                print("Invalid input! Please enter a valid number.")

        if not guessed_correctly and attempts_left == 0:
            print(f"\n😢 Out of attempts! The correct number was {number_to_guess}.")

        # Ask if the user wants to play again
        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("\nThank you for playing! Goodbye! 👋")
            break

# Run the game
number_guessing_game()



