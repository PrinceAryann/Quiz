# QuizBrain class handles the game logic and user interaction.
class QuizBrain:
    def __init__(self, question_list) -> None:
        self.question_number = 0  # Tracks the current question index.
        self.score = 0  # Tracks the user's score.
        self.question_list = question_list  # List of question objects.

    def next(self):
        # Ensure the question_number is within the range of questions available.
        if self.question_number < len(self.question_list):
            current_question = self.question_list[self.question_number]
            print(f"Your Current Score: {self.score}")
            print(f"Q{self.question_number + 1}: {current_question.text}")

            # Loop for input validation.
            while True:
                user_answer = input("Answer (True/False): ").capitalize()
                if user_answer in ["True", "False"]:
                    break

            # Check the user's answer.
            if user_answer == current_question.answer:
                print("You were Correct!")
                self.score += 1
            else:
                print("You were Wrong!")

            self.question_number += 1  # Move to the next question.
            return True
        else:
            return False  # No more questions available.
