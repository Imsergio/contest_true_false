"""Imports"""
import pathlib
import json
from question import Question
from brain import QuizBrain

RUTA = pathlib.Path(__file__).parent
with open(f"{RUTA}/data.json",mode="r",encoding="UTF8") as jdata:
    data = json.load(jdata)

question_data = data["true_false"]

question_bank = []

for question in question_data:
    q_text = question["question"]
    q_answer = question["correct_answer"]
    new_question = Question(q_text,q_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
while quiz.still_has_cuestions():
    quiz.next_question()
