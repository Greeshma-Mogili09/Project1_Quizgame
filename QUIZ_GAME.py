class Question:
    def __init__(self, question, options, answer, qtype):
        self.question = question
        self.options = options
        self.answer = answer
        self.qtype = qtype

    def ask(self):
        print(self.question)
        
        if self.qtype == "multiple-choice":
            for option in self.options:
                print(option)
            
            user_answer = input("Your answer (A, B, C, D): ").upper().strip()
            while user_answer not in ["A", "B", "C", "D"]:
                print("Invalid input. Please choose a valid option (A, B, C, or D).")
                user_answer = input("Your answer (A, B, C, D): ").upper().strip()
            
            if user_answer == self.answer:
                print("Correct!\n")
                return True
            else:
                print(f"Incorrect. The correct answer was {self.answer}.\n")
                return False

        elif self.qtype == "open-ended":
            user_answer = input("Your answer: ").strip().lower()
            
            if user_answer == self.answer.lower():
                print("Correct!\n")
                return True
            else:
                print(f"Incorrect. The correct answer was '{self.answer}'.\n")
                return False


class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0

    def run(self):
        print("Welcome to the Quiz Game!\n")
        
        for question in self.questions:
            if question.ask():
                self.score += 1
        
        self.display_results()

    def display_results(self):
        total_questions = len(self.questions)
        percentage_score = (self.score / total_questions) * 100
        
        print(f"Quiz finished! Your final score is {self.score} out of {total_questions}.")
        print(f"Your percentage score is {percentage_score:.2f}%.")
        
        passing_score = 70
        if percentage_score >= passing_score:
            print("Congratulations! You passed the quiz.")
        else:
            print("You did not pass the quiz. Better luck next time.")


def get_questions():
    return [
        Question(
            "What does 'print()' do in Python?",
            ["A) Prints a document", "B) Displays output to the console", "C) Saves a file", "D) Creates a new variable"],
            "B",
            "multiple-choice"
        ),
        Question(
            "What is the keyword used to define a function in Python?",
            ["A) func", "B) define", "C) def", "D) function"],
            "C",
            "multiple-choice"
        ),
        Question(
            "What does 'int' represent in Python?",
            ["A) A floating-point number", "B) An integer", "C) A string", "D) A list"],
            "B",
            "multiple-choice"
        ),
        Question(
            "How do you create a list in Python?",
            [],
            "list()",
            "open-ended"
        ),
        Question(
            "What will be the output of the following code: print(2 + 3 * 5)?",
            ["A) 25", "B) 17", "C) 15", "D) 20"],
            "B",
            "multiple-choice"
        ),
        Question(
            "Name the operator used for exponentiation in Python:",
            [],
            "**",
            "open-ended"
        )
    ]


if __name__ == "__main__":
    questions = get_questions()
    quiz = Quiz(questions)
    quiz.run()
