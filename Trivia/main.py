from Data import question_data
from question_model import Question
from quiz_brain import Quizbrain


question_bank = []

for i in question_data:
    question_bank.append(Question(i["question"], i["correct_answer"]))

quiz = Quizbrain(question_bank)

while quiz.still_has_questions():
    quiz.next_ques()

print(f"Your score: {quiz.score}")