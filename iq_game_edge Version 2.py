

class Question:
    def __init__(self, mcq, answer):
        self.mcq = mcq
        self.answer = answer


questions_mcqs = [

"Which of these is a type of hat?\n (a)Sausage roll\n (b)Pork pie\n (c)Scotch egg\n (d)Potato crisp\n\n",

"Which of these have to pass a test on ‘The Knowledge’ to get a licence?\n (a) Taxi drivers\n (b) Bus drivers\n (c) Police officers\n (d) Ambulance drivers\n\n",

"Which of these phrases refers to a brief success?\n (a)Blaze in the pot\n (b)Spark in the tub\n (c)Flare in the jug\n (d)Flash in the pan\n\n",

"The young of which creature is known as a squab?\n (a)Salmon\n (b)Horse\n (c)Pigeon\n (d)Octopus\n\n",

"Which of these US presidents appeared on the television series 'Laugh-In'?\n (a)Lyndon Johnson\n (b)Richard Nixon\n (c)Jimmy Carter\n (d)Gerald Ford\n\n"]

questions = [
    Question(questions_mcqs[0],"b"),
    Question(questions_mcqs[1],"a"),
    Question(questions_mcqs[2],"d"),
    Question(questions_mcqs[3],"c"),
    Question(questions_mcqs[4],"b")
]

def start_quiz(questions):
    point = 0
    for question in questions:
        answer = input(question.mcq +"Enter your answer = ")
        if answer == question.answer:
            point += 1
    print("Your totals points are " +str(point))

start_quiz(questions)

