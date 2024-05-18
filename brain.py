"""Quiz Logic"""
class QuizBrain:
    """adding a number to each question and showing the formated question
    methods: still_has_cuestions()
    methods: next_question()"""
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list

    def still_has_cuestions(self):
        """increment question number 
        ask a user response showing the current question number"""
        return self.question_number < len(self.question_list)

    def next_question(self):
        """increment question number 
        ask a user response showing the current question number"""
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        input(f"Q.{self.question_number}: {current_question.text} (True/False): ")
