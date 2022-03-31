class Question:
    def __init__(self, text_question, correct_answer, money_prize):
        self.text_question = text_question
        self.correct_answer = correct_answer
        self.money_prize = money_prize

    def correct_check(self, user_answer):
        user_answer = user_answer.lower()
        return user_answer == self.correct_answer

    def __str__(self):
        """
        String representation of questions
        :return: string representation of text question
        """
        return "___________\nGeneral question: {}" \
               "\n___________\n" \
            .format(self.text_question)

    def answer_string(self):
        """
        String representation of the answer for the question
        :return: string answer
        """
        answer = str(self.correct_answer)
        return answer

    def add_question(self, question):
        """
        Adds question to the text question
        :param question:
        """
        self.text_question = question
