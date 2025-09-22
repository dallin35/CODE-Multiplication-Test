import random


def main():
    # Randomly choose an operation from this tuple for each question
    math_operations = ("add", "subtract", "multiply")

    # Your code begins here


    main(num_questions = random.randint(1, 5)
    print("Welcome to the Random Math Quiz!")
    print(f"You will be asked {num_questions} questions")

    correct_answers = 0

    for i in range(num_questions):
        operation = random.choice(math_operations)

        # Generate numbers based on operation type
        if operation == "add":
            x = random.randint(1, 99)
            y = random.randint(1, 99)
            answer = x + y
            symbol = "+"
        elif operation == "subtract":
            x = random.randint(1, 99)
            y = random.randint(1, 99)
            answer = x - y  # negatives allowed
            symbol = "-"
        else:  # multiply
            x = random.randint(1, 12)
            y = random.randint(1, 12)
            answer = x * y
            symbol = "*"

        # Ask the question
        print(f"\nWhat is {x} {symbol} {y}?")
        try:
            user_answer = int(input("Your answer: "))
        except ValueError:
            user_answer = None  # If user enters invalid input

        # Check answer
        if user_answer == answer:
            print("Correct!")
            correct_answers += 1
        else:
            print(f"Incorrect. The answer was {answer}")

    # Final score
    print(f"\nYou got {correct_answers}/{num_questions} correct.")

