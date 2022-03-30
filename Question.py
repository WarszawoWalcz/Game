class Question:
    def __init__(self, text_question, correct_answer, money_prize):
        self.text_question = text_question
        self.correct_answer = correct_answer
        self.money_prize = money_prize

    def correct_check(self, user_answer):
        user_answer = user_answer.lower()
        return user_answer == self.correct_answer

    def __str__(self):
        return "___________\nGeneral question: {}" \
               "\nMoney: +{}\n___________\n"\
            .format(self.text_question, self.money_prize)

    def answer_string(self):
        answer = str(self.correct_answer)
        return answer

