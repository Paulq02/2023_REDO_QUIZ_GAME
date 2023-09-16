from data import question_data
from question_model import QuestionModel
import random
from random import choice
from quiz_brain import QuizBrain
from link import data_1
import json







question_data_1 = json.loads(data_1)

question_bank = []



for question in question_data_1:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = QuestionModel(question_text, question_answer)
    question_bank.append(new_question)


quiz = QuizBrain(question_bank)



while quiz.still_have_questions:
    game = quiz.next_question()
    if game == False:
        break

print("You've finished the Quiz!")
print(f"Your final score is: {quiz.correct_answers}/{quiz.question_number}")



   
    
    
        


    
    





    


