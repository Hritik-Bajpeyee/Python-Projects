import random
import time

# Define questions and answers
quiz_data = {
    "What is the capital of France?": {
        "options": ["A. Berlin", "B. Madrid", "C. Paris", "D. Rome"],
        "answer": "C"
    },
    "Which programming language is known as the backbone of web development?": {
        "options": ["A. Python", "B. JavaScript", "C. Java", "D. C++"],
        "answer": "B"
    },
    "What does RAM stand for in computer terminology?": {
        "options": ["A. Random Access Memory", "B. Read Access Memory", "C. Ready Access Module", "D. None of the above"],
        "answer": "A"
    },
    "Which planet is known as the Red Planet?": {
        "options": ["A. Earth", "B. Venus", "C. Mars", "D. Jupiter"],
        "answer": "C"
    },
    "Who wrote the novel '1984'?": {
        "options": ["A. George Orwell", "B. J.K. Rowling", "C. Ernest Hemingway", "D. Mark Twain"],
        "answer": "A"
    }
}

# Function for colorful output
def print_color(text, color="reset"):
    colors = {
        "reset": "\033[0m",
        "red": "\033[91m",
        "green": "\033[92m",
        "yellow": "\033[93m",
        "blue": "\033[94m",
        "magenta": "\033[95m"
    }
    print(f"{colors[color]}{text}{colors['reset']}")

# Welcome screen
def welcome_screen():
    print_color("✨ Welcome to the Ultimate Quiz Challenge! ✨", "magenta")
    print_color("Get ready to test your knowledge and have some fun!\n", "yellow")
    input("Press Enter to begin...\n")

# Quiz logic
def start_quiz():
    questions = list(quiz_data.items())
    random.shuffle(questions)
    score = 0

    print_color("The quiz starts now!\n", "blue")
    for idx, (question, data) in enumerate(questions, start=1):
        print_color(f"Question {idx}: {question}", "blue")
        for option in data["options"]:
            print(option)
        user_answer = input("Your answer: ").strip().upper()

        if user_answer == data["answer"]:
            print_color("Correct! 🎉\n", "green")
            score += 1
        else:
            correct_option = data["answer"]
            print_color(f"Wrong! The correct answer was {correct_option}.", "red")
            print_color("Better luck with the next one!\n", "yellow")
        time.sleep(1)  # Adds a pause for better user experience

    return score

# End screen
def display_results(score, total_questions):
    print_color("\n🏁 Quiz Completed! 🏁", "magenta")
    print_color(f"Your final score: {score}/{total_questions}\n", "yellow")

    # Personalized feedback
    if score == total_questions:
        print_color("🎉 Incredible! You're a genius! 🎉", "green")
    elif score >= total_questions * 0.7:
        print_color("👍 Great job! You did really well.", "blue")
    elif score >= total_questions * 0.4:
        print_color("🙂 Not bad, but there's room for improvement.", "yellow")
    else:
        print_color("💡 Keep learning, and you'll do better next time!", "red")

# Main function
def main():
    welcome_screen()
    score = start_quiz()
    total_questions = len(quiz_data)
    display_results(score, total_questions)

# Run the quiz app
if __name__ == "__main__":
    main()