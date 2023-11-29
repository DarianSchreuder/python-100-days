from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []

for key in range(0, len(question_data)):
    question_bank.append(Question(question_data[key]["text"],question_data[key]["answer"]))
    
quiz = QuizBrain(question_bank)
is_done = False
while is_done == False:
    
    is_done = quiz.next_question()
