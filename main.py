from question_model import Question
from data import QuestionDatabase
from quiz_brain import QuizBrain


def quiz_game():
    '''
        A fully functional quiz game.
    '''
    # Retrieving our questions
    question_db = QuestionDatabase()

    # Setting up a list of question objects to cycle through
    question_bank: list = [
        Question(question["question"], question["correct_answer"]) for question in question_db.question_data
    ]

    # Initializing the quiz
    quiz = QuizBrain(question_bank)

    # Counting our correct answers
    correct_answers: int = 0

    # Keeping the quiz alive until we've reached the end
    while not quiz.is_end_of_quiz():

        # asking a question
        quiz.ask_question()

        # evaluating if the question was answered correct
        if quiz.answer_is_correct(input("Is this [True] or [False]? ")):
            print("Correct!")
            correct_answers += 1
        else:
            print("Too bad, that was wrong!")

        # going to the next question
        quiz.count_up_question()

        # giving an indicator how many questions were answered correctly
        print(f"Correct answers: {correct_answers}/{quiz.question_number}\n\n")


if __name__ == "__main__":
    quiz_game()
