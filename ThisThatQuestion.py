from Question import Question


class ThisThatQuestion(Question):

    def __init__(self, text_question, answer1, answer2, correct_answer, money_prize, bonus):
        self.answer1 = answer1
        self.answer2 = answer2
        self.bonus = bonus
        super(ThisThatQuestion, self).__init__(text_question, correct_answer, money_prize)

        # user_answer = user_answer.lower()
        # return user_answer == self.correct_answer

    def __str__(self):
        """
        Returns string representation of ThisThatQuestion class with bonus and answer
        :return: string this or that: question + answers
        """
        return "___________\n{} or {}: {}. Additional bonus: +{}" \
               "\n___________\n".format(self.answer1, self.answer2, self.text_question, self.bonus)
