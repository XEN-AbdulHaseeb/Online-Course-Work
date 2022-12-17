from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = [Question(i['text'], i['answer']) for i in question_data]

quiz_brain = QuizBrain(question_bank)

for _ in range(len(question_bank)):
    quiz_brain.next_question()
