# Question class for creating question objects.
class Question:
    def __init__(self, text, answer) -> None:
        self.text = text  # The question text.
        self.answer = answer  # The correct answer (True/False).
