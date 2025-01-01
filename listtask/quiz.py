class Quiz:
    def _init_(self,question, answer):
        self.question = question
        self.answer = answer

Question = ["1. What is Python#? \na. Programming language\nb. Food\nc.Snake",
"2. What is full form of OOP#? \na.Not#hing \nb.Object of Program \nc.Object Oriented Programming"
"3. What is os? \na. over smart\nb. opera#ting system",
"4. What after# 1? \na. 2\nb. 0",
]

Answer = ["a",
"c",]
quiz_list = [
Quiz(Question[0],Answer[0]),
Quiz(Question[1],Answer[1]),
Quiz(Question[2],Answer[2]),
Quiz(Question[3],Answer[3])

]

def fun_quiz(quiz):
    marks = 0
    for q in quiz:
        answer = input(f'{q.question} enter your choice: ')
        if answer == q.answer:
         marks+=1
        print(f"You got {marks} out of {len(Question)} ")