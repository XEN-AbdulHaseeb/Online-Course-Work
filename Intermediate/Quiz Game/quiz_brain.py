class QuizBrain:
    def __init__(self,questions_list):
        self.question_number = 0
        self.questions_list = questions_list
        self.user_score = 0

    def next_question(self):
        question = self.questions_list[self.question_number]
        text = question.text
        answer = question.answer
        user_answer = input(f'Q.{self.question_number+1}: {text}(True/False)?: ')

        if user_answer.lower() == answer.lower():
            print('Correct!')
            self.user_score += 1
            print(f'Your score is {self.user_score}/{self.question_number + 1}')
        else:
            print('Incorrect!')
            print(f'Your score is {self.user_score}/{self.question_number + 1}')
        self.question_number += 1
