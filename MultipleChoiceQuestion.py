from Question import Question


class MultipleChoiceQuestion(Question):
    def __init__(self, text_question, answer1, answer2, answer3, answer4, correct_answer, money_prize):
        self.answer1 = answer1
        self.answer2 = answer2
        self.answer3 = answer3
        self.answer4 = answer4
        super(MultipleChoiceQuestion, self).__init__(text_question, correct_answer, money_prize)

    def __str__(self):
        """
        Returns string representation MultipleChoiceQuestion
        :return: string Choose one letter: question + possible answers
        """
        possible_answers = [self.answer1, self.answer2, self.answer3, self.answer4]
        return "___________\n{} Choose one letter: \n\n1) {}\n2) {}\n3) {}\n4) {}\n" \
               "\n___________\n".format(self.text_question, possible_answers[0], possible_answers[1],
                                        possible_answers[2], possible_answers[3])
