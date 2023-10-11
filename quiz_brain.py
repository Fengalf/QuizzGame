class QuizBrain:
    '''
        A Quiz class containing multiple methods to 
        \nrun a quiz successfully.
    '''

    def __init__(self, question_list: list):
        self.question_list = question_list
        self.question_number = 0

    def ask_question(self) -> print:
        ''' Prints the current question in the question_list.
            \nAs `self.question_number` starts at 0, the question number
            \nis incremented here by 1 to start the first question
            \noff at #1.
        '''
        print(
            f"Q.{self.question_number+1}: {self.question_list[self.question_number].text}")

    def answer_is_correct(self, answer) -> bool:
        '''
            Evaluates if the given answer is correct.
        '''
        return self.question_list[self.question_number].answer.lower() == answer.lower()

    def count_up_question(self) -> None:
        '''
            Counts up to reach the next question.
        '''
        self.question_number += 1

    def is_end_of_quiz(self) -> bool:
        '''
            Evaluates if the quiz ends by reaching the end of
            \nthe quiz list.
        '''
        return self.question_number == len(self.question_list)
