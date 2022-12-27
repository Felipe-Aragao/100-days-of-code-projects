from question_model import Question
from data import question_data
from quiz_brain import *

question_bank = []

# Create Questions objects and add than to a list
for i in question_data:
    question_text = i.get('text')
    question_answer = i.get('answer')
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print(f'You completed the quiz!')
print(f'Your score is {quiz.score}/{quiz.question_number}')
