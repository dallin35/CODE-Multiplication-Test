# CIS3330-CODE-Random-Math-Quiz

## Instructions
This program will ask the user a **random number of math questions (between 1 and 5)**. Each question will be randomly generated according to the following template: `"What is X $ Y? "` where X is the first randomly selected number, $ is a randomly selected mathematical operation, and Y is the second randomly selected number. The program will track the number of correct answers the user gives and output the final score at the end.

Randomly select mathematical operations for each question using the tuple variable provided in assignment.py

For addition questions, select 2 random numbers **between 1 and 99**
For subtraction questions, select 2 random numbers **between 1 and 99**
    **For subtraction questions, negative answers are allowed**
For multiplication questions, select 2 random numbers **between 1 and 12** 

## Prompts and Print Output
* Welcome the user and tell them how many question they will be asked:
  * `"Welcome to the Random Math Quiz!"`
  * `"You will be asked X questions"` replace X with the randomly selected number of questions
* Example question output:
  * `"\nWhat is 67 - 13?"`
  * `"\nWhat is 10 * 5?"`
  * `"\nWhat is 98 + 30?"`
  * `"\nWhat is 4 + 24?"`
  * `"\nWhat is 7 * 7?"`
* Provide feedback for each answer:
  * `"Correct!"` if they got the question right
  * `"Incorrect. The answer was X"` if they got the question wrong (replace X with the correct answer)
* Report the final score:
  * `"\nYou got X/Y correct."` replace X with the number of correct answers and Y with the number of questions asked.

## Full Example Output:

"Welcome to the Random Math Quiz!"
"You will be asked 3 questions"

"\nWhat is 86 + 22? 108
Correct!

What is 8 * 6? 48
Correct!

What is 92 - 20? 72
Correct!

You got 3/3 correct.