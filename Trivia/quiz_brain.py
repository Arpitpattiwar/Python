class Quizbrain:

    def __init__(self, q_list):
        self.question_no = 0
        self.question_list = q_list
        self.score = 0

    def next_ques(self):
        current_question = self.question_list[self.question_no]
        self.question_no += 1
        guess = input(f"Q{self.question_no}. {current_question.ques}(True/False): ")
        self.check_answer(current_question.ans, guess)


    def still_has_questions(self):
        if self.question_no == len(self.question_list):
            return False
        else:
            return True

    def check_answer(self,correct_answer, user_answer):
        if correct_answer.lower() == user_answer.lower():
            self.score += 1