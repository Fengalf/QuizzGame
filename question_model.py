class Question:
    '''
        A Question class to hold information of a question.
        \nHolds the question and an answer.
    '''

    def __init__(self, text: str, answer: str) -> None:
        self.text = text
        self.answer = answer
