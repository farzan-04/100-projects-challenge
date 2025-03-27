from data import question_data
from question_model import Question
from quiz_brain import QuizBrain


question_bank = []
for question in question_data:
    question_obj = Question(question["text"], question["answer"])
    question_bank.append(question_obj)
    #question_bank.append(Question(question["text"], question["answer"])) #this is simplified version


quiz_brain = QuizBrain(question_bank)

quiz_brain.next_question()

while quiz_brain.still_has_question():
    quiz_brain.next_question()
   
