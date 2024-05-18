"""Imports"""
from question import Question
from data import question_data
from brain import QuizBrain

question_bank = []
for question in question_data:
    QT = question["question"]
    QA = question["correct_answer"]
    new_question = Question(QT,QA)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
while quiz.still_has_cuestions():
    quiz.next_question()
