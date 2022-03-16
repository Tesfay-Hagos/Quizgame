from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
question_bank=[]
for question in question_data:
  text=question['text']
  answer=question['answer']
  questionob=Question(text,answer)
  question_bank.append(questionob)
quiz=QuizBrain(question_bank)
while(quiz.still_has_questions()):
  quiz.next_question()