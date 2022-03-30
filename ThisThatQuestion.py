from Question import Question


class ThisThatQuestion(Question):
    def __init__(self, text_question, answer1, answer2, correct_answer_index, money_prize, bonus):
        self.answer1 = answer1
        self.answer2 = answer2
        self.bonus = bonus
        self.correct_answer_index = correct_answer_index
        super(ThisThatQuestion, self).__init__(text_question, correct_answer_index, money_prize)

    def correct_check(self, user_answer):
        answers = [self.answer1, self.answer2]
        user_answer = user_answer.lower()
        return user_answer == answers[self.correct_answer_index]

    def __str__(self):
        return "___________\n{} or {}: {}. Additional bonus: +{}\nMoney: +{}" \
               "\n___________\n".format(self.answer1, self.answer2, self.text_question, self.money_prize, self.bonus)
