import requests


class QuestionDatabase:
    '''
    A QuestionDatabase that connects to opentdb and pulls questions.
    '''

    def __init__(self) -> None:
        self.request = requests.get(
            "https://opentdb.com/api.php?amount=10&category=18&difficulty=easy&type=boolean").json()
        self.question_data = self.request["results"]
