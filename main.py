# Main file for running the quiz game.
from data import question_bank
from question_model import Question
from quiz_brain import QuizBrain
import os

# Creating a list of Question objects from the question bank.
question_set = []
for items in question_bank:
    question_text = items['text']
    question_answer = items['answer']
    new_question = Question(question_text, question_answer)
    question_set.append(new_question)

# Creating an instance of QuizBrain to handle the quiz logic.
q = QuizBrain(question_set)

print("Welcome to the Quiz Game...\n")

# Loop to keep asking questions until the quiz is over.
while True:
    t = q.next()
    if not t:  # If the next question is not available (quiz ends), break the loop
        print(f"Your Final Score: {q.score}")
        break
    else:
        os.system('cls')  # This clears the screen after each question (works on Windows)
