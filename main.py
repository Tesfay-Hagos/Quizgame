from question_model import Question
from data import question_data
question_bank=[]
for question in question_data:
  text=question['text']
  answer=question['answer']
  questionob=Question(text,answer)
  question_bank.append(questionob)
print(question_bank)